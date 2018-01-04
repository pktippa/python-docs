from cmath import phase, polar
string = "4+5j" # 4 is real part and 5 is imaginary part.
in_complex_format = complex(string)

calc_r = abs(in_complex_format) # abs gives the r of polar coordinates
calc_teta = phase(in_complex_format) # phase gives the phi of polar coordinates
# We can also use polar which will give the r and phi directly as a tuple.
(calc_r_using_polar, calc_teta_using_polar) = polar(in_complex_format)