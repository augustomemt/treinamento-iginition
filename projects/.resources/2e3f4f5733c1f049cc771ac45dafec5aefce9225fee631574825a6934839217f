def doGet(request, session):
			tagPaths = [
			    "[default]Devices/pme-metrum-2/Active Power A",
			    "[default]Devices/pme-metrum-2/Current A",
			    "[default]Devices/pme-metrum-2/Current B",
			    "[default]Devices/pme-metrum-2/Voltage A-B"
			]

			try:
			    # Lê todas as tags em uma única chamada
			    qualifiedValues = system.tag.readBlocking(tagPaths, 5000)
			
			    dados = []
			
			    for index in range(len(tagPaths)):
			        qualifiedValue = qualifiedValues[index]
			
			        dados.append({
			            "tagPath": tagPaths[index],
			            "value": qualifiedValue.value,
			            "quality": str(qualifiedValue.quality),
			            "timestamp": system.date.toMillis(
			                qualifiedValue.timestamp
			            )
			        })
			
			    servletResponse = request["servletResponse"]
			
			    # Evita cache no navegador
			    servletResponse.setHeader(
			        "Cache-Control",
			        "no-store, no-cache, must-revalidate"
			    )
			
			    # Ajuste para o domínio do seu frontend
			    servletResponse.setHeader(
			        "Access-Control-Allow-Origin",
			        "*"
			    )
			
			    return {
			        "json": {
			            "success": True,
			            "serverTimestamp": system.date.toMillis(
			                system.date.now()
			            ),
			            "data": dados
			        }
			    }
			
			except Exception as error:
			    system.util.getLogger("WebDevRealtime").error(
			        "Erro ao ler tags: %s" % str(error)
			    )
			
			    request["servletResponse"].setStatus(500)
			
			    return {
			        "json": {
			            "success": False,
			            "message": "Erro ao obter dados em tempo real"
			        }
			    }