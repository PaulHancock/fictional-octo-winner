def test_module_import():
    try:
        from mymodule import sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return


def test_get_radec():
    from mymodule import sky_sim

    expected = (14.215420962967535, 41.26916666666666)
    answer = sky_sim.get_radec()

    if not( (expected[0]==answer[0]) and (expected[1]==answer[1])):
        raise AssertionError(f"get_radec gives {answer} instead of {expected}")
    return