from pymilvus import MilvusClient

def main():
    print("=== Iniciando Demostración de Milvus Lite ===")
    
    # 1. Conectar a Milvus Lite (crea un archivo local llamado milvus_demo.db)
    client = MilvusClient("./milvus_demo.db")
    
    collection_name = "demo_sentences"
    
    # Si la colección ya existe de una prueba anterior, la borramos para empezar limpios
    if client.has_collection(collection_name):
        client.drop_collection(collection_name)
        
    # 2. Crear la colección (como una tabla) indicando que usamos 4 dimensiones y distancia Coseno
    client.create_collection(
        collection_name=collection_name,
        dimension=4,
        metric_type="COSINE"
    )
    print(f"Colección '{collection_name}' creada exitosamente.")
    
    # 3. Insertar datos de prueba (vectores numéricos completos del 1 al 4 + texto descriptivo)
    data = [
        {"id": 1, "vector": [0.1, 0.2, 0.3, 0.4], "text": "El fútbol es un deporte apasionante."},
        {"id": 2, "vector": [0.1, 0.3, 0.2, 0.5], "text": "Me encanta jugar partidos de fútbol con amigos."},
        {"id": 3, "vector": [0.9, 0.8, 0.1, 0.2], "text": "La programación en Python y Node.js es muy divertida."},
        {"id": 4, "vector": [0.8, 0.9, 0.2, 0.1], "text": "Desarrollar aplicaciones web full-stack con React."}
    ]
    
    client.insert(
        collection_name=collection_name,
        data=data
    )
    print("Datos insertados correctamente en Milvus.")
    
    # 4. LLAMAR A LA FUNCIÓN DE BÚSQUEDA DE MILVUS:
    # Aquí buscamos un vector de consulta que apunta hacia la zona de deportes
    query_vector = [0.12, 0.22, 0.31, 0.42]
    
    print(f"\nEjecutando búsqueda por similitud en Milvus...")
    results = client.search(
        collection_name=collection_name,
        data=[query_vector],
        limit=2, # Queremos que devuelva los 2 resultados más cercanos
        output_fields=["text"]
    )
    
    # 5. Mostrar los resultados en consola
    print("\n--- Resultados de la Búsqueda ---")
    for hits in results:
        for hit in hits:
            print(f"ID: {hit['id']} | Distancia de Coseno: {hit['distance']:.4f} | Texto: {hit['entity']['text']}")

if __name__ == "__main__":
    main()