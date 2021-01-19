def pressureGauges(morning, evening):
    return [[min(morning[x],evening[x]) for x in range (len(morning))],[max(morning[x],evening[x]) for x in range (len(morning))]]

print(pressureGauges([129,553,585],[852,601,997])==[[129,553,585],[852,601,997]])