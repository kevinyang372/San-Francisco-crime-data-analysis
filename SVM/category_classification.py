def transform_category(data):
    new_data = []
    for i in data:
        if i == "LARCENY/THEFT":
            new_data.append("THEFT")
        elif i == "NON-CRIMINAL":
            new_data.append(i)
        elif i in ["ASSAULT","OTHER OFFENSES","SUSPICIOUS OCC","MISSING PERSON","ROBBERY","SEX OFFENSES FORCIBLE","SEX OFFENSES NON FORCIBLE","EXTORTION"]:
            new_data.append("ASSAULT")
        elif i in ["DRUG/NARCOTIC","DRUNKENNESS"]:
            new_data.append("DRUG/DRUNKENNESS")
        elif i in ["VEHICLE THEFT","VANDALISM","BURGLARY","TRESPASS"]:
            new_data.append("VEHICLE THEFT")
        else:
            new_data.append("OTHER")
    return new_data