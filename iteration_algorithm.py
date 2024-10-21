from numpy import *
import re

def convert_function(input_func):
    input_func = input_func.replace("^", "**").replace("\u00D7", "*").replace("\u00F7", "/")
    input_func = re.sub(r"(\d)(x)", r"\1*x", input_func)
    input_func = input_func.replace("\u03C0", "pi")
    input_func = re.sub(r"(\d)(pi)", r"\1*pi", input_func)

    final_func = input_func.lstrip("*")

    return final_func

def insert_func_value(func_input, x):
    func = convert_function(func_input)

    try:
        result = eval(func, {"x": x, "pi": pi, "abs": abs, "exp": exp, "sqrt": sqrt, 
                            "sin": sin, "cos": cos, "tan": tan, 
                            "log": log, "log2": log2, "log10": log10})

        return result
    except Exception as e:
        print("Error:", e)

def iteration_algorithm(func_fx, func_gx, N_iter, error, first_x):
    N_list = []; x_list = [first_x]; gx_list = []; fx_list = []
    data = []

    for iteration in range (0, N_iter):
        if iteration == 0:
            gx_list.append(round(float(insert_func_value(func_gx, x_list[iteration])), 5))
            fx_list.append(round(float(insert_func_value(func_fx, x_list[iteration])), 5))
        else:
            x_list.append(round(float(gx_list[iteration - 1]), 5))
            gx_list.append(round(float(insert_func_value(func_gx, x_list[iteration])), 5))
            fx_list.append(round(float(insert_func_value(func_fx, x_list[iteration])), 5))

        if abs(fx_list[iteration]) < error:
            final_x = x_list[N_list[iteration - 1]]

            break
        else:
            final_N = N_iter - 1

        N_list.append(iteration + 1)

    data.append(N_list)
    data.append(x_list)
    data.append(gx_list)
    data.append(fx_list)

    return data
