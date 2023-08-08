def check_arguments(**kwargs):
    # Checking arguments before the conditional
    if all(
            value is True for value in list(kwargs.values())[:5])\
            and all(value is False for value in list(kwargs.values())[5:]
                    ):
        print("arguments are ok")


# Call the function with keyword arguments
check_arguments(
    arg1=True, arg2=True, arg3=True, arg4=True, arg5=True,
    arg6=False, arg7=False, arg8=False, arg9=False, arg10=False)
