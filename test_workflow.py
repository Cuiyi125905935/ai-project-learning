"""
Simple validation script for GitHub Actions workflow testing.
This script verifies that core dependencies are working correctly.
"""

import sys


def test_imports():
    """Test that all required packages can be imported."""
    print("[TEST] Testing package imports...")
    
    try:
        import pandas as pd
        print("✓ pandas imported successfully")
    except ImportError as e:
        print(f"✗ pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✓ numpy imported successfully")
    except ImportError as e:
        print(f"✗ numpy import failed: {e}")
        return False
    
    try:
        import scipy
        print("✓ scipy imported successfully")
    except ImportError as e:
        print(f"✗ scipy import failed: {e}")
        return False
    
    try:
        import backtrader as bt
        print("✓ backtrader imported successfully")
    except ImportError as e:
        print(f"✗ backtrader import failed: {e}")
        return False
    
    try:
        import lightgbm as lgb
        print("✓ lightgbm imported successfully")
    except ImportError as e:
        print(f"✗ lightgbm import failed: {e}")
        return False
    
    try:
        import ruff
        print("✓ ruff imported successfully")
    except ImportError as e:
        print(f"✗ ruff import failed: {e}")
        # Ruff is typically used as CLI, so this is acceptable
        print("  Note: ruff is primarily a CLI tool")
    
    return True


def test_basic_functionality():
    """Test basic functionality of key packages."""
    print("\n[TEST] Testing basic functionality...")
    
    try:
        import pandas as pd
        import numpy as np
        
        # Create a simple DataFrame
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': np.random.randn(5)
        })
        print("✓ pandas DataFrame creation works")
        
        # Test numpy operations
        arr = np.array([1, 2, 3, 4, 5])
        result = np.sum(arr)
        print(f"✓ numpy operations work (sum={result})")
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False
    
    return True


def main():
    """Run all validation tests."""
    print("=" * 60)
    print("AI Alchemy System - Workflow Validation")
    print("=" * 60)
    
    success = True
    
    # Test imports
    if not test_imports():
        success = False
    
    # Test basic functionality
    if not test_basic_functionality():
        success = False
    
    print("\n" + "=" * 60)
    if success:
        print("✓ All validation tests passed!")
        print("=" * 60)
        return 0
    else:
        print("✗ Some validation tests failed!")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
