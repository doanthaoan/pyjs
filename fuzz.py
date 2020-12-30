from fuzzywuzzy import fuzz
Str1 = "Vu le code des transports, et notamment ses articles L. conseil d’administration en date du 22 juillet 2015 portant délégation de pouvoirs à son président et fixant les conditions générales des délégations au en date du 22 juillet 2015 portant"
Str2 = "Vu la délibération du conseil d’administration en date du 22 juillet 2015 portant délégation de pouvoirs à son président et fixant les conditions générales des délégations au sein de SNCF Réseau,"
Ratio = fuzz.ratio(Str1.lower(), Str2.lower())
print(Ratio)
