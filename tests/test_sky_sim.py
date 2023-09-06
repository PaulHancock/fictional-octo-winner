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


def test_make_positions_generates_correct_number_of_sources():
    from mymodule import sky_sim
    ras, decs = sky_sim.make_positions(100,0,100)
    if len(ras)!= 100:
        raise AssertionError(f"make_positions create {len(ras)} sources instead of 100")
    return