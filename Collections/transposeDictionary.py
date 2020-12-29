def transposeDictionary(scriptByExtension):
    return sorted([[b,a] for a,b in scriptByExtension.items()])
print(transposeDictionary({})==[])
print(transposeDictionary({"runSolutions": "validate","generateTests": "generateOutputs","validate": "runSolutions", "generatePeh": "generateMeh", "generateMeh": "generatePeh", "generateOutputs": "generateTests"}) == [["generateMeh","generatePeh"],["generateOutputs","generateTests"], ["generatePeh","generateMeh"], ["generateTests","generateOutputs"], ["runSolutions","validate"], ["validate","runSolutions"]])
