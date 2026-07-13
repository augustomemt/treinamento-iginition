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
	
	    <meta name="color-scheme" content="dark">
	
	    <title>PME Metrum 2 | Energy Dashboard</title>
	
	    <style>
	        :root {
	            --background: #07111f;
	            --background-secondary: #0b1728;
	            --surface: rgba(15, 29, 48, 0.86);
	            --surface-hover: rgba(20, 38, 62, 0.96);
	            --border: rgba(148, 163, 184, 0.14);
	            --text: #f8fafc;
	            --text-secondary: #91a4ba;
	            --text-muted: #64748b;
	            --green: #35d07f;
	            --red: #ff667d;
	            --blue: #42a5ff;
	            --cyan: #20d9d2;
	            --orange: #ffb454;
	            --purple: #a78bfa;
	            --shadow: 0 24px 70px rgba(0, 0, 0, 0.32);
	        }
	
	        * {
	            box-sizing: border-box;
	        }
	
	        html {
	            min-height: 100%;
	        }
	
	        body {
	            min-height: 100vh;
	            margin: 0;
	            overflow-x: hidden;
	            font-family:
	                Inter,
	                ui-sans-serif,
	                system-ui,
	                -apple-system,
	                BlinkMacSystemFont,
	                "Segoe UI",
	                sans-serif;
	            color: var(--text);
	            background:
	                radial-gradient(
	                    circle at 12% 0%,
	                    rgba(32, 217, 210, 0.13),
	                    transparent 26%
	                ),
	                radial-gradient(
	                    circle at 88% 8%,
	                    rgba(66, 165, 255, 0.13),
	                    transparent 30%
	                ),
	                linear-gradient(
	                    145deg,
	                    var(--background) 0%,
	                    var(--background-secondary) 100%
	                );
	        }
	
	        body::before {
	            content: "";
	            position: fixed;
	            inset: 0;
	            pointer-events: none;
	            opacity: 0.2;
	            background-image:
	                linear-gradient(
	                    rgba(255, 255, 255, 0.02) 1px,
	                    transparent 1px
	                ),
	                linear-gradient(
	                    90deg,
	                    rgba(255, 255, 255, 0.02) 1px,
	                    transparent 1px
	                );
	            background-size: 40px 40px;
	            mask-image:
	                linear-gradient(
	                    to bottom,
	                    black,
	                    transparent 80%
	                );
	        }
	
	        button,
	        input {
	            font: inherit;
	        }
	
	        .app {
	            position: relative;
	            z-index: 1;
	            width: min(1480px, 100%);
	            margin: 0 auto;
	            padding: 26px;
	        }
	
	        .topbar {
	            display: flex;
	            align-items: center;
	            justify-content: space-between;
	            gap: 24px;
	            margin-bottom: 32px;
	        }
	
	        .brand {
	            display: flex;
	            align-items: center;
	            gap: 15px;
	        }
	
	        .brand-icon {
	            position: relative;
	            display: grid;
	            place-items: center;
	            width: 48px;
	            height: 48px;
	            border: 1px solid rgba(32, 217, 210, 0.28);
	            border-radius: 15px;
	            color: var(--cyan);
	            background:
	                linear-gradient(
	                    145deg,
	                    rgba(32, 217, 210, 0.17),
	                    rgba(66, 165, 255, 0.07)
	                );
	            box-shadow:
	                inset 0 1px 0 rgba(255, 255, 255, 0.09),
	                0 14px 36px rgba(32, 217, 210, 0.1);
	        }
	
	        .brand-icon::after {
	            content: "";
	            position: absolute;
	            inset: -4px;
	            z-index: -1;
	            border-radius: 18px;
	            background: rgba(32, 217, 210, 0.05);
	            filter: blur(10px);
	        }
	
	        .brand-icon svg {
	            width: 25px;
	            height: 25px;
	        }
	
	        .brand h1 {
	            margin: 0;
	            font-size: clamp(20px, 3vw, 27px);
	            line-height: 1.1;
	            letter-spacing: -0.04em;
	        }
	
	        .brand p {
	            margin: 5px 0 0;
	            color: var(--text-secondary);
	            font-size: 13px;
	        }
	
	        .topbar-actions {
	            display: flex;
	            align-items: center;
	            gap: 12px;
	        }
	
	        .last-update-header,
	        .connection-badge {
	            min-height: 42px;
	            display: flex;
	            align-items: center;
	            gap: 9px;
	            padding: 0 15px;
	            border: 1px solid var(--border);
	            border-radius: 13px;
	            color: var(--text-secondary);
	            background: rgba(15, 29, 48, 0.72);
	            backdrop-filter: blur(18px);
	            box-shadow:
	                inset 0 1px 0 rgba(255, 255, 255, 0.04);
	            font-size: 12px;
	        }
	
	        .connection-badge {
	            color: #b7c5d6;
	            font-weight: 700;
	        }
	
	        .status-dot {
	            position: relative;
	            width: 9px;
	            height: 9px;
	            border-radius: 50%;
	            background: var(--orange);
	            box-shadow: 0 0 0 4px rgba(255, 180, 84, 0.1);
	        }
	
	        .status-dot::after {
	            content: "";
	            position: absolute;
	            inset: -5px;
	            border: 1px solid currentColor;
	            border-radius: 50%;
	            opacity: 0;
	        }
	
	        .status-dot.online {
	            color: var(--green);
	            background: var(--green);
	            box-shadow:
	                0 0 0 4px rgba(53, 208, 127, 0.11),
	                0 0 18px rgba(53, 208, 127, 0.42);
	        }
	
	        .status-dot.online::after {
	            animation: pulse 1.8s infinite;
	        }
	
	        .status-dot.offline {
	            color: var(--red);
	            background: var(--red);
	            box-shadow:
	                0 0 0 4px rgba(255, 102, 125, 0.11),
	                0 0 18px rgba(255, 102, 125, 0.3);
	        }
	
	        @keyframes pulse {
	            0% {
	                opacity: 0.7;
	                transform: scale(0.6);
	            }
	
	            100% {
	                opacity: 0;
	                transform: scale(1.6);
	            }
	        }
	
	        .hero {
	            position: relative;
	            overflow: hidden;
	            display: flex;
	            align-items: flex-end;
	            justify-content: space-between;
	            min-height: 150px;
	            gap: 30px;
	            margin-bottom: 20px;
	            padding: 26px 28px;
	            border: 1px solid var(--border);
	            border-radius: 24px;
	            background:
	                linear-gradient(
	                    120deg,
	                    rgba(32, 217, 210, 0.08),
	                    transparent 32%
	                ),
	                linear-gradient(
	                    150deg,
	                    rgba(15, 29, 48, 0.94),
	                    rgba(10, 23, 40, 0.9)
	                );
	            box-shadow: var(--shadow);
	            backdrop-filter: blur(20px);
	        }
	
	        .hero::after {
	            content: "";
	            position: absolute;
	            top: -100px;
	            right: -70px;
	            width: 330px;
	            height: 330px;
	            border-radius: 50%;
	            background:
	                radial-gradient(
	                    circle,
	                    rgba(66, 165, 255, 0.19),
	                    transparent 66%
	                );
	        }
	
	        .hero-copy {
	            position: relative;
	            z-index: 1;
	        }
	
	        .eyebrow {
	            display: flex;
	            align-items: center;
	            gap: 8px;
	            margin-bottom: 12px;
	            color: var(--cyan);
	            font-size: 11px;
	            font-weight: 800;
	            letter-spacing: 0.16em;
	            text-transform: uppercase;
	        }
	
	        .eyebrow-line {
	            width: 28px;
	            height: 2px;
	            border-radius: 10px;
	            background:
	                linear-gradient(
	                    to right,
	                    var(--cyan),
	                    transparent
	                );
	        }
	
	        .hero h2 {
	            max-width: 680px;
	            margin: 0;
	            font-size: clamp(25px, 4vw, 38px);
	            line-height: 1.1;
	            letter-spacing: -0.045em;
	        }
	
	        .hero p {
	            max-width: 680px;
	            margin: 13px 0 0;
	            color: var(--text-secondary);
	            font-size: 14px;
	            line-height: 1.6;
	        }
	
	        .hero-device {
	            position: relative;
	            z-index: 1;
	            flex: 0 0 auto;
	            display: flex;
	            align-items: center;
	            gap: 12px;
	            padding: 13px 16px;
	            border: 1px solid rgba(66, 165, 255, 0.17);
	            border-radius: 15px;
	            background: rgba(4, 14, 27, 0.4);
	        }
	
	        .hero-device svg {
	            width: 23px;
	            height: 23px;
	            color: var(--blue);
	        }
	
	        .hero-device-label {
	            color: var(--text-muted);
	            font-size: 10px;
	            font-weight: 800;
	            letter-spacing: 0.12em;
	            text-transform: uppercase;
	        }
	
	        .hero-device-value {
	            margin-top: 3px;
	            font-size: 13px;
	            font-weight: 750;
	        }
	
	        .error-message {
	            display: none;
	            align-items: center;
	            gap: 12px;
	            margin-bottom: 20px;
	            padding: 14px 16px;
	            border: 1px solid rgba(255, 102, 125, 0.2);
	            border-radius: 14px;
	            color: #ffc2cb;
	            background: rgba(255, 102, 125, 0.09);
	            font-size: 13px;
	        }
	
	        .error-message svg {
	            flex: 0 0 auto;
	            width: 20px;
	            height: 20px;
	        }
	
	        .cards-grid {
	            display: grid;
	            grid-template-columns:
	                repeat(4, minmax(0, 1fr));
	            gap: 16px;
	            margin-bottom: 20px;
	        }
	
	        .metric-card {
	            --accent: var(--blue);
	            position: relative;
	            overflow: hidden;
	            min-height: 190px;
	            padding: 20px;
	            border: 1px solid var(--border);
	            border-radius: 20px;
	            background:
	                linear-gradient(
	                    145deg,
	                    rgba(18, 35, 57, 0.96),
	                    rgba(10, 23, 40, 0.94)
	                );
	            box-shadow:
	                0 18px 48px rgba(0, 0, 0, 0.2),
	                inset 0 1px 0 rgba(255, 255, 255, 0.04);
	            transition:
	                transform 180ms ease,
	                border-color 180ms ease,
	                background 180ms ease;
	        }
	
	        .metric-card:hover {
	            transform: translateY(-4px);
	            border-color: color-mix(
	                in srgb,
	                var(--accent) 28%,
	                transparent
	            );
	            background:
	                linear-gradient(
	                    145deg,
	                    rgba(22, 43, 69, 0.98),
	                    rgba(11, 25, 43, 0.96)
	                );
	        }
	
	        .metric-card::before {
	            content: "";
	            position: absolute;
	            top: 0;
	            left: 20px;
	            right: 20px;
	            height: 2px;
	            border-radius: 0 0 10px 10px;
	            background:
	                linear-gradient(
	                    to right,
	                    transparent,
	                    var(--accent),
	                    transparent
	                );
	            opacity: 0.86;
	        }
	
	        .metric-card::after {
	            content: "";
	            position: absolute;
	            top: -70px;
	            right: -70px;
	            width: 180px;
	            height: 180px;
	            border-radius: 50%;
	            background: var(--accent);
	            opacity: 0.055;
	            filter: blur(4px);
	        }
	
	        .metric-power {
	            --accent: var(--orange);
	        }
	
	        .metric-current-a {
	            --accent: var(--cyan);
	        }
	
	        .metric-current-b {
	            --accent: var(--purple);
	        }
	
	        .metric-voltage {
	            --accent: var(--green);
	        }
	
	        .metric-header {
	            position: relative;
	            z-index: 1;
	            display: flex;
	            align-items: flex-start;
	            justify-content: space-between;
	            gap: 15px;
	        }
	
	        .metric-label {
	            color: var(--text-secondary);
	            font-size: 12px;
	            font-weight: 700;
	            letter-spacing: 0.015em;
	        }
	
	        .metric-subtitle {
	            margin-top: 5px;
	            color: var(--text-muted);
	            font-size: 11px;
	        }
	
	        .metric-icon {
	            display: grid;
	            place-items: center;
	            width: 40px;
	            height: 40px;
	            flex: 0 0 auto;
	            border: 1px solid
	                color-mix(
	                    in srgb,
	                    var(--accent) 24%,
	                    transparent
	                );
	            border-radius: 13px;
	            color: var(--accent);
	            background:
	                color-mix(
	                    in srgb,
	                    var(--accent) 9%,
	                    transparent
	                );
	        }
	
	        .metric-icon svg {
	            width: 21px;
	            height: 21px;
	        }
	
	        .metric-value-line {
	            position: relative;
	            z-index: 1;
	            display: flex;
	            align-items: baseline;
	            gap: 8px;
	            margin-top: 26px;
	        }
	
	        .metric-value {
	            font-size: clamp(31px, 3vw, 42px);
	            line-height: 1;
	            font-weight: 780;
	            letter-spacing: -0.055em;
	            font-variant-numeric: tabular-nums;
	        }
	
	        .metric-unit {
	            color: var(--accent);
	            font-size: 15px;
	            font-weight: 750;
	        }
	
	        .metric-footer {
	            position: relative;
	            z-index: 1;
	            display: flex;
	            align-items: center;
	            justify-content: space-between;
	            gap: 10px;
	            margin-top: 23px;
	        }
	
	        .quality-pill {
	            display: inline-flex;
	            align-items: center;
	            gap: 7px;
	            min-height: 26px;
	            padding: 0 10px;
	            border: 1px solid rgba(148, 163, 184, 0.12);
	            border-radius: 999px;
	            color: var(--text-secondary);
	            background: rgba(255, 255, 255, 0.025);
	            font-size: 10px;
	            font-weight: 750;
	        }
	
	        .quality-pill::before {
	            content: "";
	            width: 6px;
	            height: 6px;
	            border-radius: 50%;
	            background: var(--orange);
	        }
	
	        .quality-pill.good {
	            color: #86efac;
	            border-color: rgba(53, 208, 127, 0.14);
	            background: rgba(53, 208, 127, 0.07);
	        }
	
	        .quality-pill.good::before {
	            background: var(--green);
	            box-shadow: 0 0 8px rgba(53, 208, 127, 0.6);
	        }
	
	        .quality-pill.bad {
	            color: #fda4af;
	            border-color: rgba(255, 102, 125, 0.17);
	            background: rgba(255, 102, 125, 0.07);
	        }
	
	        .quality-pill.bad::before {
	            background: var(--red);
	        }
	
	        .metric-caption {
	            color: var(--text-muted);
	            font-size: 10px;
	        }
	
	        .content-grid {
	            display: grid;
	            grid-template-columns:
	                minmax(0, 1.65fr)
	                minmax(320px, 0.85fr);
	            gap: 20px;
	            align-items: stretch;
	        }
	
	        .panel {
	            overflow: hidden;
	            border: 1px solid var(--border);
	            border-radius: 22px;
	            background:
	                linear-gradient(
	                    145deg,
	                    rgba(15, 29, 48, 0.9),
	                    rgba(9, 21, 37, 0.91)
	                );
	            box-shadow:
	                0 18px 50px rgba(0, 0, 0, 0.22),
	                inset 0 1px 0 rgba(255, 255, 255, 0.035);
	            backdrop-filter: blur(18px);
	        }
	
	        .panel-header {
	            display: flex;
	            align-items: flex-start;
	            justify-content: space-between;
	            gap: 20px;
	            padding: 20px 22px 0;
	        }
	
	        .panel-title {
	            margin: 0;
	            font-size: 15px;
	            font-weight: 760;
	            letter-spacing: -0.02em;
	        }
	
	        .panel-description {
	            margin: 6px 0 0;
	            color: var(--text-muted);
	            font-size: 11px;
	        }
	
	        .chart-legend {
	            display: flex;
	            align-items: center;
	            gap: 8px;
	            color: var(--text-secondary);
	            font-size: 11px;
	            white-space: nowrap;
	        }
	
	        .chart-legend-line {
	            width: 22px;
	            height: 3px;
	            border-radius: 999px;
	            background:
	                linear-gradient(
	                    to right,
	                    var(--cyan),
	                    var(--blue)
	                );
	            box-shadow: 0 0 12px rgba(32, 217, 210, 0.3);
	        }
	
	        .chart-container {
	            position: relative;
	            height: 338px;
	            padding: 17px 14px 12px;
	        }
	
	        #powerChart {
	            width: 100%;
	            height: 100%;
	            display: block;
	        }
	
	        .chart-stats {
	            display: grid;
	            grid-template-columns: repeat(3, 1fr);
	            border-top: 1px solid var(--border);
	        }
	
	        .chart-stat {
	            padding: 16px 20px;
	        }
	
	        .chart-stat + .chart-stat {
	            border-left: 1px solid var(--border);
	        }
	
	        .chart-stat-label {
	            color: var(--text-muted);
	            font-size: 9px;
	            font-weight: 800;
	            letter-spacing: 0.12em;
	            text-transform: uppercase;
	        }
	
	        .chart-stat-value {
	            margin-top: 7px;
	            font-size: 17px;
	            font-weight: 760;
	            font-variant-numeric: tabular-nums;
	        }
	
	        .readings-panel {
	            display: flex;
	            min-height: 100%;
	            flex-direction: column;
	        }
	
	        .readings-list {
	            display: flex;
	            flex: 1;
	            flex-direction: column;
	            gap: 1px;
	            padding: 14px 14px 6px;
	        }
	
	        .reading-row {
	            display: grid;
	            grid-template-columns: 42px 1fr auto;
	            align-items: center;
	            gap: 12px;
	            min-height: 70px;
	            padding: 11px 12px;
	            border: 1px solid transparent;
	            border-radius: 14px;
	            background: rgba(255, 255, 255, 0.018);
	            transition:
	                background 160ms ease,
	                border-color 160ms ease;
	        }
	
	        .reading-row:hover {
	            border-color: var(--border);
	            background: rgba(255, 255, 255, 0.035);
	        }
	
	        .reading-icon {
	            display: grid;
	            place-items: center;
	            width: 38px;
	            height: 38px;
	            border-radius: 12px;
	            color: var(--row-accent, var(--blue));
	            background:
	                color-mix(
	                    in srgb,
	                    var(--row-accent, var(--blue)) 9%,
	                    transparent
	                );
	        }
	
	        .reading-icon svg {
	            width: 19px;
	            height: 19px;
	        }
	
	        .reading-label {
	            color: var(--text-secondary);
	            font-size: 11px;
	            font-weight: 700;
	        }
	
	        .reading-path {
	            overflow: hidden;
	            margin-top: 4px;
	            color: var(--text-muted);
	            font-size: 9px;
	            text-overflow: ellipsis;
	            white-space: nowrap;
	        }
	
	        .reading-value {
	            text-align: right;
	        }
	
	        .reading-number {
	            font-size: 16px;
	            font-weight: 780;
	            font-variant-numeric: tabular-nums;
	        }
	
	        .reading-unit {
	            margin-top: 3px;
	            color: var(--text-muted);
	            font-size: 9px;
	        }
	
	        .readings-footer {
	            display: flex;
	            align-items: center;
	            justify-content: space-between;
	            gap: 12px;
	            margin-top: auto;
	            padding: 15px 20px;
	            border-top: 1px solid var(--border);
	            color: var(--text-muted);
	            font-size: 10px;
	        }
	
	        .update-indicator {
	            display: flex;
	            align-items: center;
	            gap: 7px;
	        }
	
	        .update-spinner {
	            width: 11px;
	            height: 11px;
	            border: 2px solid rgba(148, 163, 184, 0.15);
	            border-top-color: var(--cyan);
	            border-radius: 50%;
	            opacity: 0;
	        }
	
	        .update-spinner.active {
	            opacity: 1;
	            animation: spin 0.8s linear infinite;
	        }
	
	        @keyframes spin {
	            to {
	                transform: rotate(360deg);
	            }
	        }
	
	        .footer {
	            display: flex;
	            align-items: center;
	            justify-content: space-between;
	            gap: 20px;
	            margin-top: 20px;
	            padding: 0 4px;
	            color: var(--text-muted);
	            font-size: 10px;
	        }
	
	        .footer strong {
	            color: var(--text-secondary);
	            font-weight: 700;
	        }
	
	        @media (max-width: 1120px) {
	            .cards-grid {
	                grid-template-columns: repeat(2, 1fr);
	            }
	
	            .content-grid {
	                grid-template-columns: 1fr;
	            }
	
	            .readings-list {
	                display: grid;
	                grid-template-columns: repeat(2, 1fr);
	            }
	        }
	
	        @media (max-width: 720px) {
	            .app {
	                padding: 17px;
	            }
	
	            .topbar {
	                align-items: flex-start;
	                flex-direction: column;
	                margin-bottom: 22px;
	            }
	
	            .topbar-actions {
	                width: 100%;
	            }
	
	            .last-update-header,
	            .connection-badge {
	                flex: 1;
	                justify-content: center;
	            }
	
	            .hero {
	                align-items: flex-start;
	                flex-direction: column;
	                padding: 22px;
	                border-radius: 19px;
	            }
	
	            .hero-device {
	                width: 100%;
	            }
	
	            .cards-grid {
	                grid-template-columns: 1fr;
	            }
	
	            .metric-card {
	                min-height: 175px;
	            }
	
	            .chart-container {
	                height: 280px;
	            }
	
	            .readings-list {
	                grid-template-columns: 1fr;
	            }
	
	            .panel-header {
	                flex-direction: column;
	            }
	
	            .chart-stats {
	                grid-template-columns: 1fr;
	            }
	
	            .chart-stat + .chart-stat {
	                border-top: 1px solid var(--border);
	                border-left: 0;
	            }
	
	            .footer {
	                align-items: flex-start;
	                flex-direction: column;
	            }
	        }
	
	        @media (max-width: 470px) {
	            .topbar-actions {
	                align-items: stretch;
	                flex-direction: column;
	            }
	
	            .last-update-header,
	            .connection-badge {
	                justify-content: flex-start;
	            }
	
	            .hero h2 {
	                font-size: 26px;
	            }
	        }
	    </style>
	</head>
	
	<body>
	
	<div class="app">
	
	    <header class="topbar">
	
	        <div class="brand">
	
	            <div class="brand-icon">
	                <svg
	                    viewBox="0 0 24 24"
	                    fill="none"
	                    stroke="currentColor"
	                    stroke-width="1.8"
	                    stroke-linecap="round"
	                    stroke-linejoin="round"
	                >
	                    <path d="M13 2 4.8 13.2h6.7L11 22l8.2-11.2h-6.7L13 2Z"></path>
	                </svg>
	            </div>
	
	            <div>
	                <h1>PME Metrum 2</h1>
	                <p>Energy monitoring dashboard</p>
	            </div>
	
	        </div>
	
	        <div class="topbar-actions">
	
	            <div class="last-update-header">
	                <svg
	                    width="16"
	                    height="16"
	                    viewBox="0 0 24 24"
	                    fill="none"
	                    stroke="currentColor"
	                    stroke-width="1.8"
	                    stroke-linecap="round"
	                    stroke-linejoin="round"
	                >
	                    <circle cx="12" cy="12" r="9"></circle>
	                    <path d="M12 7v5l3 2"></path>
	                </svg>
	
	                <span id="headerLastUpdate">
	                    Aguardando dados
	                </span>
	            </div>
	
	            <div class="connection-badge">
	                <span id="statusDot" class="status-dot"></span>
	                <span id="statusText">Conectando...</span>
	            </div>
	
	        </div>
	
	    </header>
	
	    <section class="hero">
	
	        <div class="hero-copy">
	
	            <div class="eyebrow">
	                <span class="eyebrow-line"></span>
	                Monitoramento em tempo real
	            </div>
	
	            <h2>
	                Vis&atilde;o instant&acirc;nea das grandezas
	                el&eacute;tricas
	            </h2>
	
	            <p>
	                Acompanhe pot&ecirc;ncia, corrente e tens&atilde;o
	                do medidor com atualiza&ccedil;&atilde;o autom&aacute;tica
	                a cada segundo.
	            </p>
	
	        </div>
	
	        <div class="hero-device">
	
	            <svg
	                viewBox="0 0 24 24"
	                fill="none"
	                stroke="currentColor"
	                stroke-width="1.8"
	                stroke-linecap="round"
	                stroke-linejoin="round"
	            >
	                <rect x="5" y="3" width="14" height="18" rx="3"></rect>
	                <path d="M8 7h8"></path>
	                <path d="M8 11h3"></path>
	                <path d="M8 15h8"></path>
	                <circle cx="15" cy="11" r="1"></circle>
	            </svg>
	
	            <div>
	                <div class="hero-device-label">
	                    Dispositivo
	                </div>
	
	                <div class="hero-device-value">
	                    pme-metrum-2
	                </div>
	            </div>
	
	        </div>
	
	    </section>
	
	    <div id="errorMessage" class="error-message">
	
	        <svg
	            viewBox="0 0 24 24"
	            fill="none"
	            stroke="currentColor"
	            stroke-width="1.8"
	            stroke-linecap="round"
	            stroke-linejoin="round"
	        >
	            <path d="M12 3 2.8 20h18.4L12 3Z"></path>
	            <path d="M12 9v4"></path>
	            <path d="M12 17h.01"></path>
	        </svg>
	
	        <span id="errorText"></span>
	
	    </div>
	
	    <section class="cards-grid">
	
	        <article class="metric-card metric-power">
	
	            <div class="metric-header">
	
	                <div>
	                    <div class="metric-label">
	                        Pot&ecirc;ncia ativa
	                    </div>
	
	                    <div class="metric-subtitle">
	                        Fase A
	                    </div>
	                </div>
	
	                <div class="metric-icon">
	                    <svg
	                        viewBox="0 0 24 24"
	                        fill="none"
	                        stroke="currentColor"
	                        stroke-width="1.8"
	                        stroke-linecap="round"
	                        stroke-linejoin="round"
	                    >
	                        <path d="M13 2 4.8 13.2h6.7L11 22l8.2-11.2h-6.7L13 2Z"></path>
	                    </svg>
	                </div>
	
	            </div>
	
	            <div class="metric-value-line">
	                <span id="activePowerA" class="metric-value">--</span>
	                <span class="metric-unit">W</span>
	            </div>
	
	            <div class="metric-footer">
	                <span
	                    id="activePowerAQuality"
	                    class="quality-pill"
	                >
	                    Aguardando
	                </span>
	
	                <span class="metric-caption">
	                    Leitura instant&acirc;nea
	                </span>
	            </div>
	
	        </article>
	
	        <article class="metric-card metric-current-a">
	
	            <div class="metric-header">
	
	                <div>
	                    <div class="metric-label">
	                        Corrente
	                    </div>
	
	                    <div class="metric-subtitle">
	                        Fase A
	                    </div>
	                </div>
	
	                <div class="metric-icon">
	                    <svg
	                        viewBox="0 0 24 24"
	                        fill="none"
	                        stroke="currentColor"
	                        stroke-width="1.8"
	                        stroke-linecap="round"
	                        stroke-linejoin="round"
	                    >
	                        <path d="M4 13c2.2-5.3 4.5-5.3 6.7 0s4.5 5.3 6.7 0"></path>
	                        <path d="M3 6h18"></path>
	                        <path d="M3 18h18"></path>
	                    </svg>
	                </div>
	
	            </div>
	
	            <div class="metric-value-line">
	                <span id="currentA" class="metric-value">--</span>
	                <span class="metric-unit">A</span>
	            </div>
	
	            <div class="metric-footer">
	                <span
	                    id="currentAQuality"
	                    class="quality-pill"
	                >
	                    Aguardando
	                </span>
	
	                <span class="metric-caption">
	                    Leitura instant&acirc;nea
	                </span>
	            </div>
	
	        </article>
	
	        <article class="metric-card metric-current-b">
	
	            <div class="metric-header">
	
	                <div>
	                    <div class="metric-label">
	                        Corrente
	                    </div>
	
	                    <div class="metric-subtitle">
	                        Fase B
	                    </div>
	                </div>
	
	                <div class="metric-icon">
	                    <svg
	                        viewBox="0 0 24 24"
	                        fill="none"
	                        stroke="currentColor"
	                        stroke-width="1.8"
	                        stroke-linecap="round"
	                        stroke-linejoin="round"
	                    >
	                        <path d="M4 13c2.2-5.3 4.5-5.3 6.7 0s4.5 5.3 6.7 0"></path>
	                        <path d="M3 6h18"></path>
	                        <path d="M3 18h18"></path>
	                    </svg>
	                </div>
	
	            </div>
	
	            <div class="metric-value-line">
	                <span id="currentB" class="metric-value">--</span>
	                <span class="metric-unit">A</span>
	            </div>
	
	            <div class="metric-footer">
	                <span
	                    id="currentBQuality"
	                    class="quality-pill"
	                >
	                    Aguardando
	                </span>
	
	                <span class="metric-caption">
	                    Leitura instant&acirc;nea
	                </span>
	            </div>
	
	        </article>
	
	        <article class="metric-card metric-voltage">
	
	            <div class="metric-header">
	
	                <div>
	                    <div class="metric-label">
	                        Tens&atilde;o
	                    </div>
	
	                    <div class="metric-subtitle">
	                        Linha A-B
	                    </div>
	                </div>
	
	                <div class="metric-icon">
	                    <svg
	                        viewBox="0 0 24 24"
	                        fill="none"
	                        stroke="currentColor"
	                        stroke-width="1.8"
	                        stroke-linecap="round"
	                        stroke-linejoin="round"
	                    >
	                        <path d="M6 4 12 20 18 4"></path>
	                        <path d="M8 10h8"></path>
	                    </svg>
	                </div>
	
	            </div>
	
	            <div class="metric-value-line">
	                <span id="voltageAB" class="metric-value">--</span>
	                <span class="metric-unit">V</span>
	            </div>
	
	            <div class="metric-footer">
	                <span
	                    id="voltageABQuality"
	                    class="quality-pill"
	                >
	                    Aguardando
	                </span>
	
	                <span class="metric-caption">
	                    Leitura instant&acirc;nea
	                </span>
	            </div>
	
	        </article>
	
	    </section>
	
	    <section class="content-grid">
	
	        <article class="panel">
	
	            <div class="panel-header">
	
	                <div>
	                    <h3 class="panel-title">
	                        Hist&oacute;rico de pot&ecirc;ncia ativa
	                    </h3>
	
	                    <p class="panel-description">
	                        &Uacute;ltimas 60 leituras recebidas da fase A
	                    </p>
	                </div>
	
	                <div class="chart-legend">
	                    <span class="chart-legend-line"></span>
	                    Active Power A
	                </div>
	
	            </div>
	
	            <div class="chart-container">
	                <canvas id="powerChart"></canvas>
	            </div>
	
	            <div class="chart-stats">
	
	                <div class="chart-stat">
	                    <div class="chart-stat-label">
	                        Atual
	                    </div>
	
	                    <div id="chartCurrent" class="chart-stat-value">
	                        -- W
	                    </div>
	                </div>
	
	                <div class="chart-stat">
	                    <div class="chart-stat-label">
	                        M&iacute;nimo
	                    </div>
	
	                    <div id="chartMinimum" class="chart-stat-value">
	                        -- W
	                    </div>
	                </div>
	
	                <div class="chart-stat">
	                    <div class="chart-stat-label">
	                        M&aacute;ximo
	                    </div>
	
	                    <div id="chartMaximum" class="chart-stat-value">
	                        -- W
	                    </div>
	                </div>
	
	            </div>
	
	        </article>
	
	        <article class="panel readings-panel">
	
	            <div class="panel-header">
	
	                <div>
	                    <h3 class="panel-title">
	                        Detalhes das leituras
	                    </h3>
	
	                    <p class="panel-description">
	                        Valores e qualidade das tags
	                    </p>
	                </div>
	
	            </div>
	
	            <div id="readingsList" class="readings-list"></div>
	
	            <div class="readings-footer">
	
	                <div class="update-indicator">
	                    <span
	                        id="updateSpinner"
	                        class="update-spinner"
	                    ></span>
	
	                    <span id="lastUpdate">
	                        Aguardando atualiza&ccedil;&atilde;o
	                    </span>
	                </div>
	
	                <span>Intervalo: 1 segundo</span>
	
	            </div>
	
	        </article>
	
	    </section>
	
	    <footer class="footer">
	        <span>
	            Sistema de monitoramento
	            <strong>PME Metrum</strong>
	        </span>
	
	        <span>
	            Web Dev &middot; Ignition Gateway
	        </span>
	    </footer>
	
	</div>
	
	<script>
	    const pathParts = window.location.pathname
	        .split("/")
	        .filter(Boolean);
	
	    const webdevIndex = pathParts.indexOf("webdev");
	
	    const projectBasePath =
	        "/" +
	        pathParts
	            .slice(0, webdevIndex + 2)
	            .join("/");
	
	    const API_URL = projectBasePath + "/real-time";
	
	    const historyValues = [];
	    const historyTimes = [];
	    const historyLimit = 60;
	
	    let requestInProgress = false;
	
	    const icons = {
	        power: `
	            <svg
	                viewBox="0 0 24 24"
	                fill="none"
	                stroke="currentColor"
	                stroke-width="1.8"
	                stroke-linecap="round"
	                stroke-linejoin="round"
	            >
	                <path d="M13 2 4.8 13.2h6.7L11 22l8.2-11.2h-6.7L13 2Z"></path>
	            </svg>
	        `,
	        current: `
	            <svg
	                viewBox="0 0 24 24"
	                fill="none"
	                stroke="currentColor"
	                stroke-width="1.8"
	                stroke-linecap="round"
	                stroke-linejoin="round"
	            >
	                <path d="M4 13c2.2-5.3 4.5-5.3 6.7 0s4.5 5.3 6.7 0"></path>
	                <path d="M3 6h18"></path>
	                <path d="M3 18h18"></path>
	            </svg>
	        `,
	        voltage: `
	            <svg
	                viewBox="0 0 24 24"
	                fill="none"
	                stroke="currentColor"
	                stroke-width="1.8"
	                stroke-linecap="round"
	                stroke-linejoin="round"
	            >
	                <path d="M6 4 12 20 18 4"></path>
	                <path d="M8 10h8"></path>
	            </svg>
	        `
	    };
	
	    const measurements = [
	        {
	            tagName: "/Active Power A",
	            label: "Pot\u00EAncia ativa",
	            detail: "Fase A",
	            unit: "W",
	            valueId: "activePowerA",
	            qualityId: "activePowerAQuality",
	            icon: "power",
	            accent: "#ffb454"
	        },
	        {
	            tagName: "/Current A",
	            label: "Corrente",
	            detail: "Fase A",
	            unit: "A",
	            valueId: "currentA",
	            qualityId: "currentAQuality",
	            icon: "current",
	            accent: "#20d9d2"
	        },
	        {
	            tagName: "/Current B",
	            label: "Corrente",
	            detail: "Fase B",
	            unit: "A",
	            valueId: "currentB",
	            qualityId: "currentBQuality",
	            icon: "current",
	            accent: "#a78bfa"
	        },
	        {
	            tagName: "/Voltage A-B",
	            label: "Tens\u00E3o",
	            detail: "Linha A-B",
	            unit: "V",
	            valueId: "voltageAB",
	            qualityId: "voltageABQuality",
	            icon: "voltage",
	            accent: "#35d07f"
	        }
	    ];
	
	    const numberFormatter = new Intl.NumberFormat(
	        "pt-BR",
	        {
	            minimumFractionDigits: 2,
	            maximumFractionDigits: 2
	        }
	    );
	
	    function findTag(data, tagName) {
	        const normalizedTagName =
	            String(tagName).toLowerCase();
	
	        return data.find(item =>
	            String(item.tagPath || "")
	                .toLowerCase()
	                .endsWith(normalizedTagName)
	        );
	    }
	
	    function formatValue(value) {
	        const number = Number(value);
	
	        if (!Number.isFinite(number)) {
	            return "--";
	        }
	
	        return numberFormatter.format(number);
	    }
	
	    function isGoodQuality(quality) {
	        return String(quality || "")
	            .toLowerCase()
	            .startsWith("good");
	    }
	
	    function escapeHtml(value) {
	        const element = document.createElement("div");
	        element.textContent = String(value ?? "");
	        return element.innerHTML;
	    }
	
	    function updateQuality(elementId, quality) {
	        const element = document.getElementById(elementId);
	
	        if (!element) {
	            return;
	        }
	
	        const good = isGoodQuality(quality);
	
	        element.textContent = good
	            ? "Qualidade: Good"
	            : "Qualidade: " + String(quality || "Indispon\u00EDvel");
	
	        element.className = good
	            ? "quality-pill good"
	            : "quality-pill bad";
	    }
	
	    function updateCard(measurement, tag) {
	        const valueElement =
	            document.getElementById(measurement.valueId);
	
	        if (!tag) {
	            valueElement.textContent = "--";
	
	            updateQuality(
	                measurement.qualityId,
	                "Tag n\u00E3o encontrada"
	            );
	
	            return;
	        }
	
	        valueElement.textContent =
	            formatValue(tag.value);
	
	        updateQuality(
	            measurement.qualityId,
	            tag.quality
	        );
	    }
	
	    function createReadingRow(measurement, tag) {
	        const qualityGood =
	            tag && isGoodQuality(tag.quality);
	
	        const value =
	            tag ? formatValue(tag.value) : "--";
	
	        const tagPath =
	            tag
	                ? tag.tagPath
	                : "Tag n\u00E3o encontrada";
	
	        return `
	            <div
	                class="reading-row"
	                style="--row-accent: ${measurement.accent}"
	            >
	                <div class="reading-icon">
	                    ${icons[measurement.icon]}
	                </div>
	
	                <div>
	                    <div class="reading-label">
	                        ${escapeHtml(measurement.label)}
	                        &middot;
	                        ${escapeHtml(measurement.detail)}
	                    </div>
	
	                    <div class="reading-path">
	                        ${escapeHtml(tagPath)}
	                    </div>
	                </div>
	
	                <div class="reading-value">
	                    <div class="reading-number">
	                        ${escapeHtml(value)}
	                    </div>
	
	                    <div class="reading-unit">
	                        ${escapeHtml(measurement.unit)}
	                        &middot;
	                        ${
	                            qualityGood
	                                ? "Good"
	                                : "Indispon\u00EDvel"
	                        }
	                    </div>
	                </div>
	            </div>
	        `;
	    }
	
	    function updateReadingsList(data) {
	        const list =
	            document.getElementById("readingsList");
	
	        list.innerHTML = measurements
	            .map(measurement => {
	                const tag = findTag(
	                    data,
	                    measurement.tagName
	                );
	
	                return createReadingRow(
	                    measurement,
	                    tag
	                );
	            })
	            .join("");
	    }
	
	    function setConnectionStatus(online, text) {
	        const dot =
	            document.getElementById("statusDot");
	
	        const statusText =
	            document.getElementById("statusText");
	
	        dot.className = online
	            ? "status-dot online"
	            : "status-dot offline";
	
	        statusText.textContent = text;
	    }
	
	    function setLoading(loading) {
	        document
	            .getElementById("updateSpinner")
	            .classList.toggle("active", loading);
	    }
	
	    function showError(message) {
	        document.getElementById(
	            "errorText"
	        ).textContent = message;
	
	        document.getElementById(
	            "errorMessage"
	        ).style.display = "flex";
	    }
	
	    function hideError() {
	        document.getElementById(
	            "errorMessage"
	        ).style.display = "none";
	    }
	
	    function addPowerHistory(value, timestamp) {
	        const number = Number(value);
	
	        if (!Number.isFinite(number)) {
	            return;
	        }
	
	        historyValues.push(number);
	        historyTimes.push(timestamp || Date.now());
	
	        if (historyValues.length > historyLimit) {
	            historyValues.shift();
	            historyTimes.shift();
	        }
	
	        updateChartStats();
	        drawChart();
	    }
	
	    function updateChartStats() {
	        if (historyValues.length === 0) {
	            return;
	        }
	
	        const current =
	            historyValues[historyValues.length - 1];
	
	        const minimum =
	            Math.min(...historyValues);
	
	        const maximum =
	            Math.max(...historyValues);
	
	        document.getElementById(
	            "chartCurrent"
	        ).textContent =
	            formatValue(current) + " W";
	
	        document.getElementById(
	            "chartMinimum"
	        ).textContent =
	            formatValue(minimum) + " W";
	
	        document.getElementById(
	            "chartMaximum"
	        ).textContent =
	            formatValue(maximum) + " W";
	    }
	
	    function prepareCanvas() {
	        const canvas =
	            document.getElementById("powerChart");
	
	        const rect =
	            canvas.getBoundingClientRect();
	
	        const dpr =
	            window.devicePixelRatio || 1;
	
	        const expectedWidth =
	            Math.max(1, Math.floor(rect.width * dpr));
	
	        const expectedHeight =
	            Math.max(1, Math.floor(rect.height * dpr));
	
	        if (
	            canvas.width !== expectedWidth ||
	            canvas.height !== expectedHeight
	        ) {
	            canvas.width = expectedWidth;
	            canvas.height = expectedHeight;
	        }
	
	        const context =
	            canvas.getContext("2d");
	
	        context.setTransform(
	            dpr,
	            0,
	            0,
	            dpr,
	            0,
	            0
	        );
	
	        return {
	            canvas,
	            context,
	            width: rect.width,
	            height: rect.height
	        };
	    }
	
	    function drawChart() {
	        const {
	            context,
	            width,
	            height
	        } = prepareCanvas();
	
	        context.clearRect(
	            0,
	            0,
	            width,
	            height
	        );
	
	        const padding = {
	            top: 24,
	            right: 20,
	            bottom: 36,
	            left: 58
	        };
	
	        const chartWidth =
	            width - padding.left - padding.right;
	
	        const chartHeight =
	            height - padding.top - padding.bottom;
	
	        if (
	            chartWidth <= 0 ||
	            chartHeight <= 0
	        ) {
	            return;
	        }
	
	        if (historyValues.length === 0) {
	            context.fillStyle = "#64748b";
	            context.font =
	                "12px system-ui, sans-serif";
	
	            context.fillText(
	                "Aguardando dados...",
	                padding.left,
	                height / 2
	            );
	
	            return;
	        }
	
	        const minimum =
	            Math.min(...historyValues);
	
	        const maximum =
	            Math.max(...historyValues);
	
	        const visibleRange =
	            maximum - minimum;
	
	        const margin =
	            Math.max(
	                visibleRange * 0.18,
	                Math.abs(maximum) * 0.003,
	                0.5
	            );
	
	        const chartMinimum =
	            minimum - margin;
	
	        const chartMaximum =
	            maximum + margin;
	
	        const range =
	            chartMaximum - chartMinimum || 1;
	
	        context.lineWidth = 1;
	        context.font =
	            "10px system-ui, sans-serif";
	        context.textAlign = "right";
	        context.textBaseline = "middle";
	
	        for (let index = 0; index <= 4; index++) {
	            const ratio =
	                index / 4;
	
	            const y =
	                padding.top +
	                chartHeight * ratio;
	
	            context.beginPath();
	            context.moveTo(padding.left, y);
	            context.lineTo(
	                width - padding.right,
	                y
	            );
	
	            context.strokeStyle =
	                "rgba(148, 163, 184, 0.10)";
	
	            context.stroke();
	
	            const value =
	                chartMaximum -
	                range * ratio;
	
	            context.fillStyle = "#64748b";
	
	            context.fillText(
	                Number(value).toLocaleString(
	                    "pt-BR",
	                    {
	                        maximumFractionDigits: 1
	                    }
	                ),
	                padding.left - 11,
	                y
	            );
	        }
	
	        const getX = index => {
	            if (historyValues.length === 1) {
	                return padding.left;
	            }
	
	            return (
	                padding.left +
	                chartWidth *
	                index /
	                (historyValues.length - 1)
	            );
	        };
	
	        const getY = value => {
	            return (
	                padding.top +
	                chartHeight -
	                (
	                    (value - chartMinimum) /
	                    range *
	                    chartHeight
	                )
	            );
	        };
	
	        const fillGradient =
	            context.createLinearGradient(
	                0,
	                padding.top,
	                0,
	                height - padding.bottom
	            );
	
	        fillGradient.addColorStop(
	            0,
	            "rgba(32, 217, 210, 0.28)"
	        );
	
	        fillGradient.addColorStop(
	            0.55,
	            "rgba(66, 165, 255, 0.10)"
	        );
	
	        fillGradient.addColorStop(
	            1,
	            "rgba(66, 165, 255, 0)"
	        );
	
	        context.beginPath();
	
	        historyValues.forEach(
	            (value, index) => {
	                const x = getX(index);
	                const y = getY(value);
	
	                if (index === 0) {
	                    context.moveTo(x, y);
	                } else {
	                    context.lineTo(x, y);
	                }
	            }
	        );
	
	        context.lineTo(
	            getX(historyValues.length - 1),
	            height - padding.bottom
	        );
	
	        context.lineTo(
	            getX(0),
	            height - padding.bottom
	        );
	
	        context.closePath();
	        context.fillStyle = fillGradient;
	        context.fill();
	
	        const lineGradient =
	            context.createLinearGradient(
	                padding.left,
	                0,
	                width - padding.right,
	                0
	            );
	
	        lineGradient.addColorStop(
	            0,
	            "#20d9d2"
	        );
	
	        lineGradient.addColorStop(
	            1,
	            "#42a5ff"
	        );
	
	        context.beginPath();
	
	        historyValues.forEach(
	            (value, index) => {
	                const x = getX(index);
	                const y = getY(value);
	
	                if (index === 0) {
	                    context.moveTo(x, y);
	                } else {
	                    context.lineTo(x, y);
	                }
	            }
	        );
	
	        context.strokeStyle = lineGradient;
	        context.lineWidth = 2.4;
	        context.lineJoin = "round";
	        context.lineCap = "round";
	        context.shadowColor =
	            "rgba(32, 217, 210, 0.25)";
	        context.shadowBlur = 10;
	        context.stroke();
	        context.shadowBlur = 0;
	
	        const lastIndex =
	            historyValues.length - 1;
	
	        const lastX =
	            getX(lastIndex);
	
	        const lastY =
	            getY(historyValues[lastIndex]);
	
	        context.beginPath();
	        context.arc(
	            lastX,
	            lastY,
	            5,
	            0,
	            Math.PI * 2
	        );
	
	        context.fillStyle = "#07111f";
	        context.fill();
	
	        context.beginPath();
	        context.arc(
	            lastX,
	            lastY,
	            3.1,
	            0,
	            Math.PI * 2
	        );
	
	        context.fillStyle = "#20d9d2";
	        context.fill();
	
	        context.textAlign = "left";
	        context.textBaseline = "alphabetic";
	    }
	
	    function updateTimestamp(timestamp) {
	        const date =
	            timestamp
	                ? new Date(timestamp)
	                : new Date();
	
	        const formatted =
	            date.toLocaleString(
	                "pt-BR",
	                {
	                    day: "2-digit",
	                    month: "2-digit",
	                    year: "numeric",
	                    hour: "2-digit",
	                    minute: "2-digit",
	                    second: "2-digit"
	                }
	            );
	
	        document.getElementById(
	            "lastUpdate"
	        ).textContent =
	            "Atualizado em " + formatted;
	
	        document.getElementById(
	            "headerLastUpdate"
	        ).textContent =
	            "Atualizado " +
	            date.toLocaleTimeString(
	                "pt-BR",
	                {
	                    hour: "2-digit",
	                    minute: "2-digit",
	                    second: "2-digit"
	                }
	            );
	    }
	
	    async function loadRealtimeData() {
	        if (requestInProgress) {
	            return;
	        }
	
	        requestInProgress = true;
	        setLoading(true);
	
	        try {
	            const response = await fetch(
	                API_URL,
	                {
	                    method: "GET",
	                    cache: "no-store",
	                    headers: {
	                        "Accept": "application/json"
	                    }
	                }
	            );
	
	            if (!response.ok) {
	                throw new Error(
	                    "Erro HTTP " + response.status
	                );
	            }
	
	            const result =
	                await response.json();
	
	            if (!result.success) {
	                throw new Error(
	                    result.message ||
	                    "A API retornou um erro."
	                );
	            }
	
	            const data =
	                Array.isArray(result.data)
	                    ? result.data
	                    : [];
	
	            measurements.forEach(
	                measurement => {
	                    const tag = findTag(
	                        data,
	                        measurement.tagName
	                    );
	
	                    updateCard(
	                        measurement,
	                        tag
	                    );
	                }
	            );
	
	            updateReadingsList(data);
	
	            const activePower = findTag(
	                data,
	                "/Active Power A"
	            );
	
	            if (
	                activePower &&
	                isGoodQuality(activePower.quality)
	            ) {
	                addPowerHistory(
	                    activePower.value,
	                    activePower.timestamp
	                );
	            }
	
	            updateTimestamp(
	                result.serverTimestamp
	            );
	
	            hideError();
	
	            setConnectionStatus(
	                true,
	                "Conectado"
	            );
	
	        } catch (error) {
	            console.error(error);
	
	            setConnectionStatus(
	                false,
	                "Sem conex\u00E3o"
	            );
	
	            showError(
	                "N\u00E3o foi poss\u00EDvel carregar os dados: " +
	                error.message
	            );
	
	        } finally {
	            requestInProgress = false;
	            setLoading(false);
	        }
	    }
	
	    window.addEventListener(
	        "resize",
	        drawChart
	    );
	
	    drawChart();
	    updateReadingsList([]);
	    loadRealtimeData();
	
	    setInterval(
	        loadRealtimeData,
	        1000
	    );
	</script>
	
	</body>
	</html>
	"""
	
	response = request["servletResponse"]
	
	response.setCharacterEncoding("UTF-8")
	response.setContentType("text/html; charset=UTF-8")
	
	response.setHeader(
	    "Cache-Control",
	    "no-store, no-cache, must-revalidate, max-age=0"
	)
	
	response.setHeader(
	    "Pragma",
	    "no-cache"
	)
	
	writer = response.getWriter()
	writer.write(html)
	writer.flush()
	
	return None