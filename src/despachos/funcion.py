def calcular_tarifa_despacho(peso_kg: float, distancia_km: float, es_prioritario: bool = False) -> float:
    """
    Calcula el costo total de un despacho basado en el peso, distancia y urgencia.
    """
    if peso_kg <= 0 or distancia_km <= 0:
        raise ValueError("El peso y la distancia deben ser mayores a cero.")
        
    # Tarifa base fija por operación
    tarifa_base = 1500.0
    
    # Costo por peso (tarifa escalonada)
    if peso_kg < 5.0:
        costo_peso = peso_kg * 250.0
    elif peso_kg <= 20.0:
        costo_peso = peso_kg * 400.0
    else:
        costo_peso = peso_kg * 600.0  # Sobrecargo por exceso de peso
        
    # Costo por distancia recorrida
    if distancia_km < 10.0:
        costo_distancia = 0.0  # Envío local gratuito en los primeros kilómetros
    else:
        costo_distancia = (distancia_km - 10.0) * 120.0
        
    # Cálculo inicial
    subtotal = tarifa_base + costo_peso + costo_distancia
    
    # Modificadores por tipo de servicio
    if es_prioritario:
        total = subtotal * 1.30  # 30% de recargo por envío express
    else:
        total = subtotal
        
    return round(total, 2)
