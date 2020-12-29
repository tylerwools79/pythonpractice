from collections import Counter
#a simple function that takes a string and returns the most common character in that string
def frequencyAnalysis(encryptedText):
    return Counter(encryptedText).most_common(1)[0][0]
print(frequencyAnalysis("$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ")=="C")
print(frequencyAnalysis("Agoodglassinthebishop'shostelinthedevil'sseattwenty-onedegreesandthirteenminutesnortheastandbynorthmainbranchseventhlimbeastsideshootfromthelefteyeofthedeath's-headabeelinefromthetreethroughtheshotfiftyfeetout.")=="e")
print(frequencyAnalysis("Q")=="Q")
print(frequencyAnalysis("):<<}:BnUUKc=>~LKU><,;U><U=~BKc=>~}~jKB;UU~n== ~c=fS<c~}~:w~~Unc}=>Kw=~~ceKc*=~Uc<w=>~nU=nc}Lfc<w=>enKcLwncY>U~j~c=>BKeL~nU=UK}~U><<=mw<e=>~B~m=~f~<m=>~}~n=>;US>~n}nL~~BKc~mw<e=>~=w~~=>w<*:>=>~U><=mKm=fm~~=<*=k")=="~")
