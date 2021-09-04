def FarenheitConverter(FarenheitValue):
    CelciuesValue = (FarenheitValue - 32) * 5/9
    CelciuesValue = round(CelciuesValue,2)
    return CelciuesValue

print("Your farenhait value is this many degrees celcius: ")
print(FarenheitConverter(45))
