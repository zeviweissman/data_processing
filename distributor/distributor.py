def distributor(initial_data, *funcs):
    for func in funcs:
        func(initial_data)
