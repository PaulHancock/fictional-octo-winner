def test_module_import():
    try:
        from mymodule import sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return