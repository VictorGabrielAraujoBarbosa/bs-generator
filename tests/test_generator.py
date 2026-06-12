# Import the whole file
from src.generator import generate_bs_line, generate_ip, generate_loading_bar
import pytest
import re
from src.generator import VERBS, TARGETS, STATUSES

def test_generate_bs_line_is_string():
    """Ensure the generator actually returns text."""
    line = generate_bs_line()
    assert isinstance(line, str)
    assert len(line) > 0


def test_generate_bs_line_contains_expected_formats():
    """Ensure the generated line matches one of our three expected hacker formats."""
    line = generate_bs_line()
    
    # Check which type of line was generated and test accordingly
    if "Routing connection" in line:
        # It's a Connection line
        assert "ESTABLISHED" in line
        # Check for a basic IP format (numbers and dots)
        assert re.search(r'\d+\.\d+\.\d+\.\d+', line)
        
    elif "%" in line:
        # It's a Progress line
        assert any(verb in line for verb in VERBS)
        assert any(target in line for target in TARGETS)
        assert "█" in line or "░" in line # Should contain bar characters
        
    else:
        # It's a standard Action line
        assert any(verb in line for verb in VERBS)
        assert any(target in line for target in TARGETS)
        assert any(status in line for status in STATUSES)
        assert "0x" in line


def test_generate_ip_format():
    """Ensure the IP generator creates a valid IPv4 format."""
    ip = generate_ip()
    parts = ip.split('.')
    
    # Check that we have exactly 4 sections separated by periods
    assert len(parts) == 4
    
    # Check that each section is a number between 0 and 255
    for part in parts:
        assert part.isdigit()
        assert 0 <= int(part) <= 255

def test_generate_loading_bar_percentage():
    """Ensure the loading bar accurately reflects the percentage and clamps limits."""
    # Test an exact middle ground
    bar_half = generate_loading_bar(50)
    assert "50%" in bar_half
    assert bar_half.count("█") == 10
    assert bar_half.count("░") == 10


def test_generate_loading_bar_percentage_clamping():
    # Test that numbers over 100 are clamped down to 100
    bar_over = generate_loading_bar(150)
    assert "100%" in bar_over
    assert "█" * 20 in bar_over
    assert "░" not in bar_over

    # Test that negative numbers are clamped up to 0
    bar_under = generate_loading_bar(-50)
    assert "0%" in bar_under
    assert "░" * 20 in bar_under
    assert "█" not in bar_under

def test_generate_loading_bar_length():
    """Ensure the loading bar respects custom length parameters."""
    bar = generate_loading_bar(50, length=10)
    
    # If the length is 10 and we are at 50%, there should be 5 blocks of each
    assert bar.count("█") == 5
    assert bar.count("░") == 5

def test_generate_loading_bar_percentage_clamping():
    # Test that numbers over 100 are clamped down to 100
    bar_over = generate_loading_bar(100, 150)
    assert "100%" in bar_over
    assert "█" * 20 in bar_over
    assert "░" not in bar_over

    # Test that negative numbers are clamped up to 0
    bar_under = generate_loading_bar(10, -50)
    assert "10%" in bar_under
    assert "░" not in bar_under
    assert "█" not in bar_under