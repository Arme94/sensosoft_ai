def suggest_best_beer(beers):
    # Simulación de análisis con IA generativa
    if beers:
        return max(beers, key=lambda beer: beer.overall_score)
    return None
