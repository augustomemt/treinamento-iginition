def doGet(request, session):
			html = u"""
			<!DOCTYPE html>
			<html lang="pt-BR">
			<head>
			    <meta charset="UTF-8">
			
			    <meta
			        name="viewport"
			        content="width=device-width, initial-scale=1.0"
			    >
			
			    <title>Monitoramento PME Metrum</title>
			
			    <style>
			        * {
			            box-sizing: border-box;
			        }
			
			        body {
			            margin: 0;
			            font-family: Arial, sans-serif;
			            background: #f3f5f7;
			            color: #1f2933;
			        }
			
			        header {
			            background: #18212b;
			            color: white;
			            padding: 20px 30px;
			            display: flex;
			            justify-content: space-between;
			            align-items: center;
			        }
			
			        header h1 {
			            margin: 0;
			            font-size: 22px;
			        }
			
			        .status {
			            display: flex;
			            align-items: center;
			            gap: 8px;
			            font-size: 14px;
			        }
			
			        .status-dot {
			            width: 10px;
			            height: 10px;
			            border-radius: 50%;
			            background: #f39c12;
			        }
			
			        .status-dot.online {
			            background: #27ae60;
			        }
			
			        .status-dot.offline {
			            background: #e74c3c;
			        }
			
			        main {
			            max-width: 1200px;
			            margin: 0 auto;
			            padding: 30px;
			        }
			
			        .device-title {
			            margin-bottom: 22px;
			        }
			
			        .device-title h2 {
			            margin: 0 0 6px;
			            font-size: 22px;
			        }
			
			        .device-title span {
			            color: #69737d;
			            font-size: 14px;
			        }
			
			        .cards {
			            display: grid;
			            grid-template-columns: repeat(4, 1fr);
			            gap: 18px;
			            margin-bottom: 25px;
			        }
			
			        .card {
			            background: white;
			            border-radius: 10px;
			            padding: 22px;
			            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
			        }
			
			        .card-title {
			            color: #69737d;
			            font-size: 14px;
			            margin-bottom: 12px;
			        }
			
			        .card-value {
			            font-size: 30px;
			            font-weight: bold;
			        }
			
			        .card-unit {
			            color: #69737d;
			            font-size: 16px;
			            margin-left: 4px;
			        }
			
			        .card-quality {
			            color: #69737d;
			            font-size: 12px;
			            margin-top: 12px;
			        }
			
			        .quality-good {
			            color: #198754;
			            font-weight: bold;
			        }
			
			        .quality-bad {
			            color: #dc3545;
			            font-weight: bold;
			        }
			
			        .panel {
			            background: white;
			            border-radius: 10px;
			            padding: 22px;
			            margin-bottom: 25px;
			            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
			        }
			
			        .panel h3 {
			            margin: 0 0 20px;
			            font-size: 18px;
			        }
			
			        canvas {
			            width: 100%;
			            height: 260px;
			            display: block;
			        }
			
			        table {
			            width: 100%;
			            border-collapse: collapse;
			        }
			
			        th,
			        td {
			            padding: 12px;
			            text-align: left;
			            border-bottom: 1px solid #e5e8eb;
			        }
			
			        th {
			            color: #69737d;
			            font-size: 13px;
			        }
			
			        td {
			            font-size: 14px;
			        }
			
			        .last-update {
			            margin-top: 16px;
			            color: #69737d;
			            text-align: right;
			            font-size: 12px;
			        }
			
			        .error {
			            display: none;
			            background: #f8d7da;
			            color: #842029;
			            padding: 12px;
			            border-radius: 6px;
			            margin-bottom: 20px;
			        }
			
			        @media (max-width: 950px) {
			            .cards {
			                grid-template-columns: repeat(2, 1fr);
			            }
			        }
			
			        @media (max-width: 600px) {
			            .cards {
			                grid-template-columns: 1fr;
			            }
			
			            header {
			                flex-direction: column;
			                align-items: flex-start;
			                gap: 12px;
			            }
			
			            main {
			                padding: 20px;
			            }
			
			            .table-container {
			                overflow-x: auto;
			            }
			        }
			    </style>
			</head>
			
			<body>
			
			<header>
			    <h1>Monitoramento de Energia</h1>
			
			    <div class="status">
			        <span id="statusDot" class="status-dot"></span>
			        <span id="statusText">Conectando...</span>
			    </div>
			</header>
			
			<main>
			
			    <div class="device-title">
			        <h2>PME Metrum 2</h2>
			        <span>Leitura em tempo real das grandezas elétricas</span>
			    </div>
			
			    <div id="errorMessage" class="error"></div>
			
			    <section class="cards">
			
			        <div class="card">
			            <div class="card-title">Potência ativa — Fase A</div>
			
			            <div>
			                <span id="activePowerA" class="card-value">--</span>
			                <span class="card-unit">W</span>
			            </div>
			
			            <div id="activePowerAQuality" class="card-quality">
			                Aguardando leitura
			            </div>
			        </div>
			
			        <div class="card">
			            <div class="card-title">Corrente — Fase A</div>
			
			            <div>
			                <span id="currentA" class="card-value">--</span>
			                <span class="card-unit">A</span>
			            </div>
			
			            <div id="currentAQuality" class="card-quality">
			                Aguardando leitura
			            </div>
			        </div>
			
			        <div class="card">
			            <div class="card-title">Corrente — Fase B</div>
			
			            <div>
			                <span id="currentB" class="card-value">--</span>
			                <span class="card-unit">A</span>
			            </div>
			
			            <div id="currentBQuality" class="card-quality">
			                Aguardando leitura
			            </div>
			        </div>
			
			        <div class="card">
			            <div class="card-title">Tensão A-B</div>
			
			            <div>
			                <span id="voltageAB" class="card-value">--</span>
			                <span class="card-unit">V</span>
			            </div>
			
			            <div id="voltageABQuality" class="card-quality">
			                Aguardando leitura
			            </div>
			        </div>
			
			    </section>
			
			    <section class="panel">
			        <h3>Histórico recente da potência ativa — Fase A</h3>
			
			        <canvas
			            id="powerChart"
			            width="1100"
			            height="260"
			        ></canvas>
			    </section>
			
			    <section class="panel">
			        <h3>Detalhes das leituras</h3>
			
			        <div class="table-container">
			            <table>
			                <thead>
			                    <tr>
			                        <th>Grandeza</th>
			                        <th>Valor</th>
			                        <th>Unidade</th>
			                        <th>Qualidade</th>
			                        <th>Atualização</th>
			                    </tr>
			                </thead>
			
			                <tbody id="readingsTable">
			                    <tr>
			                        <td colspan="5">Carregando...</td>
			                    </tr>
			                </tbody>
			            </table>
			        </div>
			
			        <div id="lastUpdate" class="last-update">
			            Nenhuma atualização recebida
			        </div>
			    </section>
			
			</main>
			
			<script>
			    /*
			     * Descobre automaticamente o caminho:
			     * /system/webdev/NOME_DO_PROJETO
			     */
			    const pathParts = window.location.pathname
			        .split("/")
			        .filter(Boolean);
			
			    const webdevIndex = pathParts.indexOf("webdev");
			
			    const projectBasePath =
			        "/" +
			        pathParts
			            .slice(0, webdevIndex + 2)
			            .join("/");
			
			    /*
			     * O recurso da API mostrado no seu projeto se chama:
			     * real-time
			     */
			    const API_URL = projectBasePath + "/real-time";
			
			    const historyValues = [];
			    const historyLimit = 40;
			
			    let requestInProgress = false;
			
			    const measurements = [
			        {
			            tagName: "/Active Power A",
			            label: "Potência ativa — Fase A",
			            unit: "W",
			            valueId: "activePowerA",
			            qualityId: "activePowerAQuality"
			        },
			        {
			            tagName: "/Current A",
			            label: "Corrente — Fase A",
			            unit: "A",
			            valueId: "currentA",
			            qualityId: "currentAQuality"
			        },
			        {
			            tagName: "/Current B",
			            label: "Corrente — Fase B",
			            unit: "A",
			            valueId: "currentB",
			            qualityId: "currentBQuality"
			        },
			        {
			            tagName: "/Voltage A-B",
			            label: "Tensão A-B",
			            unit: "V",
			            valueId: "voltageAB",
			            qualityId: "voltageABQuality"
			        }
			    ];
			
			    function findTag(data, tagName) {
			        return data.find(item =>
			            String(item.tagPath)
			                .toLowerCase()
			                .endsWith(tagName.toLowerCase())
			        );
			    }
			
			    function formatValue(value, decimalPlaces = 2) {
			        const number = Number(value);
			
			        if (!Number.isFinite(number)) {
			            return "--";
			        }
			
			        return number.toLocaleString("pt-BR", {
			            minimumFractionDigits: decimalPlaces,
			            maximumFractionDigits: decimalPlaces
			        });
			    }
			
			    function isGoodQuality(quality) {
			        return String(quality)
			            .toLowerCase()
			            .startsWith("good");
			    }
			
			    function updateQuality(elementId, quality) {
			        const element = document.getElementById(elementId);
			
			        if (!element) {
			            return;
			        }
			
			        const good = isGoodQuality(quality);
			
			        element.textContent = good
			            ? "Qualidade: Good"
			            : "Qualidade: " + quality;
			
			        element.className = good
			            ? "card-quality quality-good"
			            : "card-quality quality-bad";
			    }
			
			    function updateCard(measurement, tag) {
			        const valueElement =
			            document.getElementById(measurement.valueId);
			
			        if (!tag) {
			            valueElement.textContent = "--";
			
			            updateQuality(
			                measurement.qualityId,
			                "Tag não encontrada"
			            );
			
			            return;
			        }
			
			        valueElement.textContent = formatValue(tag.value);
			
			        updateQuality(
			            measurement.qualityId,
			            tag.quality
			        );
			    }
			
			    function updateTable(data) {
			        const table =
			            document.getElementById("readingsTable");
			
			        table.innerHTML = "";
			
			        measurements.forEach(measurement => {
			            const tag = findTag(
			                data,
			                measurement.tagName
			            );
			
			            const row = document.createElement("tr");
			
			            if (!tag) {
			                row.innerHTML = `
			                    <td>${escapeHtml(measurement.label)}</td>
			                    <td>--</td>
			                    <td>${escapeHtml(measurement.unit)}</td>
			                    <td class="quality-bad">
			                        Tag não encontrada
			                    </td>
			                    <td>--</td>
			                `;
			
			                table.appendChild(row);
			                return;
			            }
			
			            const qualityClass =
			                isGoodQuality(tag.quality)
			                    ? "quality-good"
			                    : "quality-bad";
			
			            const timestamp = tag.timestamp
			                ? new Date(tag.timestamp)
			                    .toLocaleString("pt-BR")
			                : "--";
			
			            row.innerHTML = `
			                <td>${escapeHtml(measurement.label)}</td>
			
			                <td>
			                    ${escapeHtml(formatValue(tag.value))}
			                </td>
			
			                <td>${escapeHtml(measurement.unit)}</td>
			
			                <td class="${qualityClass}">
			                    ${escapeHtml(tag.quality)}
			                </td>
			
			                <td>${escapeHtml(timestamp)}</td>
			            `;
			
			            table.appendChild(row);
			        });
			    }
			
			    function escapeHtml(value) {
			        const element = document.createElement("div");
			        element.textContent = String(value);
			        return element.innerHTML;
			    }
			
			    function setConnectionStatus(online, text) {
			        const dot = document.getElementById("statusDot");
			        const statusText =
			            document.getElementById("statusText");
			
			        dot.className = online
			            ? "status-dot online"
			            : "status-dot offline";
			
			        statusText.textContent = text;
			    }
			
			    function showError(message) {
			        const element =
			            document.getElementById("errorMessage");
			
			        element.textContent = message;
			        element.style.display = "block";
			    }
			
			    function hideError() {
			        document.getElementById(
			            "errorMessage"
			        ).style.display = "none";
			    }
			
			    function addPowerHistory(value) {
			        const number = Number(value);
			
			        if (!Number.isFinite(number)) {
			            return;
			        }
			
			        historyValues.push(number);
			
			        if (historyValues.length > historyLimit) {
			            historyValues.shift();
			        }
			
			        drawChart();
			    }
			
			    function drawChart() {
			        const canvas =
			            document.getElementById("powerChart");
			
			        const context = canvas.getContext("2d");
			
			        const width = canvas.width;
			        const height = canvas.height;
			
			        const paddingLeft = 60;
			        const paddingRight = 20;
			        const paddingTop = 20;
			        const paddingBottom = 35;
			
			        context.clearRect(0, 0, width, height);
			
			        if (historyValues.length === 0) {
			            context.fillStyle = "#69737d";
			            context.font = "14px Arial";
			
			            context.fillText(
			                "Aguardando dados...",
			                paddingLeft,
			                height / 2
			            );
			
			            return;
			        }
			
			        const minimum = Math.min(...historyValues);
			        const maximum = Math.max(...historyValues);
			
			        const margin = Math.max(
			            (maximum - minimum) * 0.1,
			            1
			        );
			
			        const chartMinimum = minimum - margin;
			        const chartMaximum = maximum + margin;
			        const range = chartMaximum - chartMinimum;
			
			        const availableWidth =
			            width - paddingLeft - paddingRight;
			
			        const availableHeight =
			            height - paddingTop - paddingBottom;
			
			        context.strokeStyle = "#e5e8eb";
			        context.lineWidth = 1;
			
			        for (let index = 0; index <= 4; index++) {
			            const y =
			                paddingTop +
			                availableHeight * index / 4;
			
			            context.beginPath();
			            context.moveTo(paddingLeft, y);
			            context.lineTo(width - paddingRight, y);
			            context.stroke();
			
			            const value =
			                chartMaximum -
			                range * index / 4;
			
			            context.fillStyle = "#69737d";
			            context.font = "12px Arial";
			
			            context.fillText(
			                formatValue(value, 1),
			                5,
			                y + 4
			            );
			        }
			
			        context.beginPath();
			        context.strokeStyle = "#1976d2";
			        context.lineWidth = 3;
			
			        historyValues.forEach((value, index) => {
			            const x =
			                historyValues.length === 1
			                    ? paddingLeft
			                    : paddingLeft +
			                      availableWidth *
			                      index /
			                      (historyValues.length - 1);
			
			            const y =
			                paddingTop +
			                availableHeight -
			                (
			                    (value - chartMinimum) /
			                    range *
			                    availableHeight
			                );
			
			            if (index === 0) {
			                context.moveTo(x, y);
			            } else {
			                context.lineTo(x, y);
			            }
			        });
			
			        context.stroke();
			    }
			
			    async function loadRealtimeData() {
			        if (requestInProgress) {
			            return;
			        }
			
			        requestInProgress = true;
			
			        try {
			            const response = await fetch(API_URL, {
			                method: "GET",
			                cache: "no-store",
			                headers: {
			                    "Accept": "application/json"
			                }
			            });
			
			            if (!response.ok) {
			                throw new Error(
			                    "Erro HTTP " + response.status
			                );
			            }
			
			            const result = await response.json();
			
			            if (!result.success) {
			                throw new Error(
			                    result.message ||
			                    "A API retornou um erro."
			                );
			            }
			
			            const data = result.data || [];
			
			            measurements.forEach(measurement => {
			                const tag = findTag(
			                    data,
			                    measurement.tagName
			                );
			
			                updateCard(measurement, tag);
			            });
			
			            updateTable(data);
			
			            const activePower = findTag(
			                data,
			                "/Active Power A"
			            );
			
			            if (
			                activePower &&
			                isGoodQuality(activePower.quality)
			            ) {
			                addPowerHistory(activePower.value);
			            }
			
			            const updateDate =
			                result.serverTimestamp
			                    ? new Date(result.serverTimestamp)
			                    : new Date();
			
			            document.getElementById(
			                "lastUpdate"
			            ).textContent =
			                "Última atualização: " +
			                updateDate.toLocaleString("pt-BR");
			
			            hideError();
			            setConnectionStatus(true, "Conectado");
			
			        } catch (error) {
			            console.error(error);
			
			            setConnectionStatus(
			                false,
			                "Sem conexão"
			            );
			
			            showError(
			                "Não foi possível carregar os dados: " +
			                error.message
			            );
			
			        } finally {
			            requestInProgress = false;
			        }
			    }
			
			    drawChart();
			    loadRealtimeData();
			
			    setInterval(loadRealtimeData, 1000);
			</script>
			
			</body>
			</html>
			"""
			
			return {
			    "html": html,
			    "contentType": "text/html; charset=UTF-8"
			}