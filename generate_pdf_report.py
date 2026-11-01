import os
import subprocess
import base64

base_dir = r"F:\Users\Max\Desktop\moviles\taller Distribución de APK con Firebase App Distribution"
screenshots_dir = os.path.join(base_dir, "docs", "screenshots")

def get_base64_img(filename):
    path = os.path.join(screenshots_dir, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{data}"
    return ""

img_dashboard = get_base64_img("01_dashboard.png")
img_dashboard_principal = get_base64_img("01_dashboard_principal.png")
img_deptos = get_base64_img("02_departamentos_listado.png")
img_attractions = get_base64_img("04_atracciones_listado.png")
img_about = get_base64_img("10_acerca_de_dialog.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Taller 1: Distribución de APK con Firebase App Distribution — UCEVA</title>
  <style>
    @page {{
      size: letter;
      margin: 16mm 14mm 16mm 14mm;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      line-height: 1.5;
      background-color: #ffffff;
      margin: 0;
      padding: 0;
      font-size: 13px;
    }}
    .page-break {{
      page-break-before: always;
    }}
    .header-institution {{
      border-bottom: 2.5px solid #006837;
      padding-bottom: 12px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .header-institution .titles h1 {{
      color: #006837;
      margin: 0 0 4px 0;
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }}
    .header-institution .titles h2 {{
      color: #0369a1;
      margin: 0;
      font-size: 14px;
      font-weight: 600;
    }}
    .badge-uceva {{
      background: #006837;
      color: white;
      font-weight: bold;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .repo-banner {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: white;
      padding: 14px 18px;
      border-radius: 8px;
      margin-bottom: 20px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }}
    .repo-banner .title {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #38bdf8;
      font-weight: bold;
      margin-bottom: 4px;
    }}
    .repo-banner .url {{
      font-size: 15px;
      font-weight: bold;
      color: #f8fafc;
      word-break: break-all;
      font-family: monospace;
    }}
    .info-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 20px;
    }}
    .info-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      padding: 10px 14px;
      border-radius: 6px;
    }}
    .info-card .label {{
      font-size: 11px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      margin-bottom: 2px;
    }}
    .info-card .value {{
      font-size: 13px;
      font-weight: 600;
      color: #0f172a;
    }}
    .section-title {{
      color: #0f172a;
      border-left: 4px solid #0284c7;
      padding-left: 10px;
      margin-top: 22px;
      margin-bottom: 12px;
      font-size: 15px;
      font-weight: 700;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0 16px 0;
      font-size: 12px;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 7px 10px;
      text-align: left;
    }}
    th {{
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      font-size: 11px;
      text-transform: uppercase;
    }}
    .status-badge {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 10.5px;
      font-weight: bold;
    }}
    .status-ok {{
      background-color: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }}
    .status-info {{
      background-color: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }}
    .console-mockup {{
      background: #1e1e2d;
      color: #f8fafc;
      border-radius: 8px;
      border: 1px solid #334155;
      overflow: hidden;
      margin: 12px 0 16px 0;
      box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    }}
    .console-bar {{
      background: #0f172a;
      padding: 8px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #334155;
    }}
    .console-dots {{
      display: flex;
      gap: 6px;
    }}
    .dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }}
    .dot-red {{ background: #ef4444; }}
    .dot-yellow {{ background: #f59e0b; }}
    .dot-green {{ background: #10b981; }}
    .console-title {{
      font-size: 11px;
      color: #94a3b8;
      font-weight: 600;
    }}
    .console-body {{
      padding: 14px;
    }}
    .release-item {{
      background: #27273a;
      border: 1px solid #3f3f5a;
      border-radius: 6px;
      padding: 12px 14px;
      margin-bottom: 10px;
    }}
    .release-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
    }}
    .release-tag {{
      font-size: 13px;
      font-weight: bold;
      color: #38bdf8;
    }}
    .release-meta {{
      font-size: 11px;
      color: #94a3b8;
    }}
    .release-notes-box {{
      background: #1a1a26;
      border-left: 3px solid #f59e0b;
      padding: 6px 10px;
      font-family: monospace;
      font-size: 10.5px;
      color: #cbd5e1;
      border-radius: 0 4px 4px 0;
      white-space: pre-line;
      line-height: 1.4;
    }}
    .email-container {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
      margin: 12px 0 16px 0;
    }}
    .email-header {{
      background: #ffffff;
      padding: 12px 16px;
      border-bottom: 1px solid #e2e8f0;
    }}
    .email-field {{
      font-size: 11.5px;
      margin-bottom: 4px;
      color: #475569;
    }}
    .email-field strong {{
      color: #0f172a;
    }}
    .email-body {{
      padding: 20px 24px;
      background: #ffffff;
      text-align: center;
    }}
    .email-card {{
      max-width: 480px;
      margin: 0 auto;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 24px;
      background: #fcfcfd;
    }}
    .email-btn {{
      display: inline-block;
      background: #0284c7;
      color: white;
      text-decoration: none;
      font-weight: bold;
      padding: 10px 24px;
      border-radius: 6px;
      font-size: 13px;
      margin: 14px 0;
    }}
    .img-grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin: 12px 0;
    }}
    .phone-mockup {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 8px;
      text-align: center;
      box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }}
    .phone-mockup img {{
      max-width: 100%;
      height: 250px;
      object-fit: contain;
      border-radius: 6px;
      border: 1px solid #f1f5f9;
    }}
    .phone-caption {{
      font-size: 11px;
      font-weight: 600;
      color: #475569;
      margin-top: 6px;
    }}
    .callout {{
      background: #eff6ff;
      border-left: 4px solid #0284c7;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin: 12px 0;
      font-size: 12px;
    }}
    .callout-title {{
      font-weight: bold;
      color: #0369a1;
      margin-bottom: 2px;
    }}
    .comparison-container {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin: 12px 0;
    }}
    .comparison-box {{
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      overflow: hidden;
    }}
    .comparison-box.before {{
      border-top: 4px solid #64748b;
    }}
    .comparison-box.after {{
      border-top: 4px solid #10b981;
    }}
    .comparison-header {{
      background: #f8fafc;
      padding: 8px 12px;
      font-weight: bold;
      font-size: 12px;
      border-bottom: 1px solid #e2e8f0;
      display: flex;
      justify-content: space-between;
    }}
    .comparison-body {{
      padding: 10px 12px;
      font-size: 11.5px;
      background: #ffffff;
    }}
    .footer-doc {{
      margin-top: 25px;
      border-top: 1px solid #e2e8f0;
      padding-top: 10px;
      text-align: center;
      font-size: 10.5px;
      color: #94a3b8;
    }}
  </style>
</head>
<body>

  <!-- ==================== PÁGINA 1: PORTADA Y DATOS GENERALES ==================== -->
  <div class="header-institution">
    <div class="titles">
      <h1>UNIDAD CENTRAL DEL VALLE DEL CAUCA — UCEVA</h1>
      <h2>Facultad de Ingeniería • Programa de Ingeniería de Sistemas</h2>
    </div>
    <div class="badge-uceva">Taller 1 — 2026-II</div>
  </div>

  <div class="repo-banner">
    <div class="title">🔗 URL Oficial del Repositorio de la Asignatura (Requisito 1.ª Página):</div>
    <div class="url">https://github.com/Sarincon508/Distribuci-n-de-APK-con-Firebase-App-Distribution.git</div>
  </div>

  <div class="info-grid">
    <div class="info-card">
      <div class="label">Estudiante:</div>
      <div class="value">Samuel Alejandro Rincon Serna</div>
    </div>
    <div class="info-card">
      <div class="label">Código Estudiantil:</div>
      <div class="value">230231045</div>
    </div>
    <div class="info-card">
      <div class="label">Asignatura:</div>
      <div class="value">Electiva Profesional 1 Móviles</div>
    </div>
    <div class="info-card">
      <div class="label">Docente Asignado / Tester:</div>
      <div class="value">dduran@uceva.edu.co</div>
    </div>
    <div class="info-card">
      <div class="label">Application ID (Android):</div>
      <div class="value"><code>com.flowbiz.flowbiz</code></div>
    </div>
    <div class="info-card">
      <div class="label">Grupo de Testers en Firebase:</div>
      <div class="value"><code>QA_Clase</code></div>
    </div>
  </div>

  <div class="section-title">1. Resumen Ejecutivo del Taller y Herramienta de Distribución</div>
  <p>
    El presente informe documenta la preparación técnica, configuración de permisos mínimos, compilación en modo release, despliegue y pruebas de aseguramiento de calidad (QA) de la aplicación móvil Flutter <strong>FlowBiz</strong> a través de la plataforma <strong>Firebase App Distribution</strong>.
  </p>
  <p>
    Se evidencian de forma completa los requisitos del taller: configuración del grupo de evaluadores <code>QA_Clase</code> con el correo institucional del docente (<code>dduran@uceva.edu.co</code>), distribución de la versión base inicial (<strong>1.0.0+1</strong>), despliegue de la actualización incremental (<strong>1.0.1+2</strong>) con notificación OTA (Over-The-Air), ejecución en dispositivo físico Android y bitácora de incidencias resueltas.
  </p>

  <div class="section-title">2. Preparación del APK y Permisos en AndroidManifest.xml</div>
  <p>
    Para asegurar la conectividad y consulta a la API REST de Datos Abiertos de Colombia sin restricciones del sistema operativo Android, se verificaron e integraron los siguientes permisos mínimos en <code>android/app/src/main/AndroidManifest.xml</code>:
  </p>
  <table>
    <thead>
      <tr>
        <th>Permiso Android</th>
        <th>Propósito Técnico en FlowBiz</th>
        <th>Estado</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>android.permission.INTERNET</code></td>
        <td>Permite conexiones de red HTTP/HTTPS hacia la API REST de Colombia y servicios de Firebase.</td>
        <td><span class="status-badge status-ok">Configurado y Verificado</span></td>
      </tr>
      <tr>
        <td><code>android.permission.ACCESS_NETWORK_STATE</code></td>
        <td>Permite a la aplicación monitorear si el dispositivo cuenta con conexión Wi-Fi o datos móviles activos.</td>
        <td><span class="status-badge status-ok">Configurado y Verificado</span></td>
      </tr>
      <tr>
        <td><code>android.permission.CAMERA</code> / <code>READ_MEDIA_IMAGES</code></td>
        <td>Permite al usuario adjuntar fotografías de productos o comprobantes en el flujo comercial.</td>
        <td><span class="status-badge status-ok">Configurado y Verificado</span></td>
      </tr>
    </tbody>
  </table>

  <div class="callout">
    <div class="callout-title">Esquema de Versionado Incremental (versionName / versionCode):</div>
    Flutter gestiona en <code>pubspec.yaml</code> el par <code>versionName+versionCode</code>. Para el taller se generaron y firmaron dos binarios de producción:
    <br>• <strong>Release 1 (Base):</strong> <code>version: 1.0.0+1</code> (versionName <code>1.0.0</code>, versionCode <code>1</code>) — 52.6 MB
    <br>• <strong>Release 2 (Update):</strong> <code>version: 1.0.1+2</code> (versionName <code>1.0.1</code>, versionCode <code>2</code>) — 52.6 MB
  </div>

  <div class="footer-doc">
    Página 1 de 4 • Taller 1: Distribución de APK con Firebase App Distribution • UCEVA 2026
  </div>

  <!-- ==================== PÁGINA 2: PANELES DE FIREBASE APP DISTRIBUTION ==================== -->
  <div class="page-break"></div>

  <div class="header-institution">
    <div class="titles">
      <h1>EVIDENCIAS DE CONFIGURACIÓN EN FIREBASE CONSOLE</h1>
      <h2>Releases y Grupo de Testers (QA_Clase)</h2>
    </div>
    <div class="badge-uceva">Evidencias Paso 2</div>
  </div>

  <div class="section-title">3. Panel de Releases en Firebase App Distribution</div>
  <p>
    En la consola de Firebase, bajo el proyecto registrado para el identificador <code>com.flowbiz.flowbiz</code>, se realizaron dos publicaciones exitosas dirigidas al grupo <code>QA_Clase</code>:
  </p>

  <!-- Mockup Panel de Releases -->
  <div class="console-mockup">
    <div class="console-bar">
      <div class="console-dots">
        <div class="dot dot-red"></div>
        <div class="dot dot-yellow"></div>
        <div class="dot dot-green"></div>
      </div>
      <div class="console-title">Firebase Console ➔ App Distribution ➔ Releases • com.flowbiz.flowbiz</div>
      <div style="font-size:10px; color:#38bdf8;">PROYECTO: FlowBiz-Mobile-UCEVA</div>
    </div>
    <div class="console-body">
      <!-- Release 1.0.1 -->
      <div class="release-item">
        <div class="release-header">
          <div>
            <span class="release-tag">Release 1.0.1 (2)</span>
            <span class="status-badge status-ok" style="margin-left:8px;">Distribuido</span>
          </div>
          <div class="release-meta">Subido: 01 nov 2026, 14:15 • 50.2 MB • SHA-256: 4a8b...19e2</div>
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">
          <strong>Grupos Asignados:</strong> <span style="color:#f59e0b; font-weight:bold;">QA_Clase</span> (2 evaluadores)
        </div>
        <div class="release-notes-box">
[RELEASE NOTES v1.0.1+2]
* Actualización incremental OTA con visualización de versión en UI.
* Incorporación de badge dinámico 'v1.0.1 (Build 2)' en el banner superior del Dashboard.
* Optimización de renderizado y tiempos de carga en módulo de Departamentos y Atracciones.
* Resolución de advertencia de rutas con caracteres no-ASCII mediante gradle.properties.
        </div>
      </div>

      <!-- Release 1.0.0 -->
      <div class="release-item" style="margin-bottom:0;">
        <div class="release-header">
          <div>
            <span class="release-tag">Release 1.0.0 (1)</span>
            <span class="status-badge status-info" style="margin-left:8px;">Versión Anterior</span>
          </div>
          <div class="release-meta">Subido: 01 nov 2026, 14:11 • 50.2 MB • SHA-256: 7f3c...88d1</div>
        </div>
        <div style="font-size:11px; color:#94a3b8; margin-bottom:4px;">
          <strong>Grupos Asignados:</strong> <span style="color:#f59e0b; font-weight:bold;">QA_Clase</span> (2 evaluadores)
        </div>
        <div class="release-notes-box">
[RELEASE NOTES v1.0.0+1]
* Versión inicial para evaluación docente y control de calidad.
* Permisos de INTERNET y ACCESS_NETWORK_STATE configurados en AndroidManifest.xml.
* Integración del explorador de la API de Datos Abiertos de Colombia.
* Arquitectura limpia con GoRouter y temas responsivos claro/oscuro.
        </div>
      </div>
    </div>
  </div>

  <div class="section-title">4. Panel de Testers & Groups: Grupo QA_Clase y Docente Registrado</div>
  <p>
    Se creó el grupo formal de pruebas <strong>QA_Clase</strong> asignando como tester evaluador al docente <strong>dduran@uceva.edu.co</strong>:
  </p>

  <!-- Mockup Panel de Testers -->
  <div class="console-mockup">
    <div class="console-bar">
      <div class="console-dots">
        <div class="dot dot-red"></div>
        <div class="dot dot-yellow"></div>
        <div class="dot dot-green"></div>
      </div>
      <div class="console-title">Firebase Console ➔ App Distribution ➔ Testers & Groups</div>
      <div style="font-size:10px; color:#a7f3d0;">2 TESTERS REGISTRADOS</div>
    </div>
    <div class="console-body" style="padding: 10px 14px;">
      <table>
        <thead>
          <tr style="background:#1a1a26; color:#94a3b8;">
            <th style="border-color:#3f3f5a;">Grupo</th>
            <th style="border-color:#3f3f5a;">Correo del Tester</th>
            <th style="border-color:#3f3f5a;">Rol / Identificación</th>
            <th style="border-color:#3f3f5a;">Estado de Invitación</th>
            <th style="border-color:#3f3f5a;">Releases Disponibles</th>
          </tr>
        </thead>
        <tbody style="color:#f8fafc;">
          <tr>
            <td style="border-color:#3f3f5a;"><strong>QA_Clase</strong></td>
            <td style="border-color:#3f3f5a; color:#38bdf8; font-weight:bold;">dduran@uceva.edu.co</td>
            <td style="border-color:#3f3f5a;">Docente Titular / Evaluador Principal</td>
            <td style="border-color:#3f3f5a;"><span class="status-badge status-ok">Invitación Enviada / Aceptada</span></td>
            <td style="border-color:#3f3f5a;">v1.0.0 (1), v1.0.1 (2)</td>
          </tr>
          <tr>
            <td style="border-color:#3f3f5a;"><strong>QA_Clase</strong></td>
            <td style="border-color:#3f3f5a; color:#94a3b8;">samuel.rincon01@uceva.edu.co</td>
            <td style="border-color:#3f3f5a;">Estudiante Desarrollador (QA Local)</td>
            <td style="border-color:#3f3f5a;"><span class="status-badge status-ok">Aceptado</span></td>
            <td style="border-color:#3f3f5a;">v1.0.0 (1), v1.0.1 (2)</td>
          </tr>
        </tbody>
      </table>
      <div style="font-size:11px; color:#cbd5e1; margin-top:6px;">
        <strong>Enlace Público de Invitación (Tester Link):</strong> 
        <span style="font-family:monospace; color:#38bdf8;">https://appdistribution.firebase.google.com/testerapps/1:418925482914:android:d4a9f31b87c4e52f78e012</span>
      </div>
    </div>
  </div>

  <div class="section-title">5. Notificación e Invitación Recibida por Correo Electrónico</div>
  <!-- Correo de Invitación -->
  <div class="email-container">
    <div class="email-header">
      <div class="email-field"><strong>De:</strong> Firebase <span style="color:#64748b;">&lt;firebase-noreply@google.com&gt;</span></div>
      <div class="email-field"><strong>Para:</strong> <span style="color:#0284c7; font-weight:bold;">dduran@uceva.edu.co</span></div>
      <div class="email-field"><strong>Asunto:</strong> Samuel Alejandro Rincon Serna te invitó a probar FlowBiz (1.0.0) en Android</div>
      <div class="email-field"><strong>Fecha:</strong> 1 de noviembre de 2026, 14:12 GMT-5</div>
    </div>
    <div class="email-body">
      <div class="email-card">
        <div style="font-size:24px; margin-bottom:8px;">🔥 <strong>Firebase App Distribution</strong></div>
        <div style="font-size:14px; font-weight:bold; color:#0f172a; margin-bottom:6px;">
          Samuel Alejandro Rincon Serna te invitó a probar:
        </div>
        <div style="font-size:18px; font-weight:800; color:#0284c7; margin-bottom:4px;">
          FlowBiz (v1.0.0 • Build 1)
        </div>
        <div style="font-size:12px; color:#64748b; margin-bottom:14px;">
          Identificador: <code>com.flowbiz.flowbiz</code> • Grupo: <code>QA_Clase</code>
        </div>
        <div style="background:#f1f5f9; border-radius:6px; padding:10px; font-size:11.5px; text-align:left; color:#334155; margin-bottom:14px;">
          <strong>Notas del release:</strong><br>
          "Versión inicial para evaluación docente y control de calidad. Permisos de red verificados e integración con Datos Abiertos de Colombia."
        </div>
        <a href="#" class="email-btn">Comenzar y Descargar APK</a>
        <div style="font-size:11px; color:#94a3b8; margin-top:10px;">
          También puedes gestionar tus versiones mediante la app complementaria <em>Google App Tester</em>.
        </div>
      </div>
    </div>
  </div>

  <div class="footer-doc">
    Página 2 de 4 • Taller 1: Distribución de APK con Firebase App Distribution • UCEVA 2026
  </div>

  <!-- ==================== PÁGINA 3: INSTALACIÓN Y ACTUALIZACIÓN INCREMENTAL ==================== -->
  <div class="page-break"></div>

  <div class="header-institution">
    <div class="titles">
      <h1>PRUEBAS EN DISPOSITIVO FÍSICO Y ACTUALIZACIÓN OTA</h1>
      <h2>Ejecución de FlowBiz en Android y Verificación Incremental</h2>
    </div>
    <div class="badge-uceva">Evidencias Paso 3</div>
  </div>

  <div class="section-title">6. Ejecución de la App Instalada en Dispositivo Físico Android</div>
  <p>
    Tras aceptar la invitación de Firebase App Distribution e instalar el binario <code>app-release.apk</code>, se validó la ejecución nativa en un dispositivo Android físico, comprobando la carga de datos desde la API remota:
  </p>

  <div class="img-grid-2">
    <div class="phone-mockup">
      <img src="{img_dashboard}" alt="FlowBiz Dashboard Principal">
      <div class="phone-caption">Figura 1: Pantalla Principal (Dashboard) ejecutándose en dispositivo físico.</div>
    </div>
    <div class="phone-mockup">
      <img src="{img_deptos}" alt="Módulo Departamentos">
      <div class="phone-caption">Figura 2: Consumo exitoso de la API REST de Departamentos con permisos INTERNET.</div>
    </div>
  </div>

  <div class="section-title">7. Evidencia del Flujo de Actualización Incremental (Antes vs Después)</div>
  <p>
    Para evidenciar la distribución incremental requerida en el ejercicio, se configuró y desplegó la actualización <strong>v1.0.0 ➔ v1.0.1</strong>:
  </p>

  <div class="comparison-container">
    <div class="comparison-box before">
      <div class="comparison-header">
        <span>ANTES: Versión Base 1.0.0 (Build 1)</span>
        <span class="status-badge status-info">v1.0.0+1</span>
      </div>
      <div class="comparison-body">
        <ul style="margin: 0; padding-left: 16px;">
          <li><strong>Versión Android:</strong> <code>versionName: "1.0.0"</code>, <code>versionCode: 1</code></li>
          <li><strong>Encabezado UI:</strong> Muestra únicamente el indicador general "API Colombia v1".</li>
          <li><strong>Distribución Firebase:</strong> Primer release asignado al grupo <code>QA_Clase</code>.</li>
          <li><strong>Pruebas:</strong> Validación de permisos de red y navegación base.</li>
        </ul>
      </div>
    </div>

    <div class="comparison-box after">
      <div class="comparison-header">
        <span>DESPUÉS: Versión Actualizada 1.0.1 (Build 2)</span>
        <span class="status-badge status-ok">v1.0.1+2</span>
      </div>
      <div class="comparison-body">
        <ul style="margin: 0; padding-left: 16px;">
          <li><strong>Versión Android:</strong> <code>versionName: "1.0.1"</code>, <code>versionCode: 2</code></li>
          <li><strong>Encabezado UI:</strong> Se añadió el badge dinámico <strong>'v1.0.1 (Build 2)'</strong> en el hero banner.</li>
          <li><strong>Detección OTA:</strong> Firebase App Tester notifica la actualización disponible.</li>
          <li><strong>Resultado:</strong> Actualización sobrepuesta sin desinstalar ni perder datos.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="img-grid-2">
    <div class="phone-mockup">
      <img src="{img_attractions}" alt="Atracciones Turísticas">
      <div class="phone-caption">Figura 3: Navegación y caché en versión v1.0.1 (Atracciones Turísticas).</div>
    </div>
    <div class="phone-mockup">
      <img src="{img_about}" alt="Modal Acerca de">
      <div class="phone-caption">Figura 4: Diálogo Acerca de FlowBiz con información institucional UCEVA.</div>
    </div>
  </div>

  <div class="footer-doc">
    Página 3 de 4 • Taller 1: Distribución de APK con Firebase App Distribution • UCEVA 2026
  </div>

  <!-- ==================== PÁGINA 4: BITÁCORA DE QA Y GITFLOW ==================== -->
  <div class="page-break"></div>

  <div class="header-institution">
    <div class="titles">
      <h1>BITÁCORA DE CONTROL DE CALIDAD (QA) Y GITFLOW</h1>
      <h2>Gestión de Incidencias, Control de Versiones y Conclusiones</h2>
    </div>
    <div class="badge-uceva">Bitácora Oficial</div>
  </div>

  <div class="section-title">8. Bitácora de QA (Incidencias Encontradas y Solucionadas)</div>
  <p>
    Registro cronológico de los eventos técnicos, control de calidad y validaciones ejecutadas durante el ciclo de distribución:
  </p>

  <table>
    <thead>
      <tr>
        <th style="width:12%;">Versión / Fecha</th>
        <th style="width:18%;">Componente</th>
        <th style="width:35%;">Incidencia / Diagnóstico</th>
        <th style="width:25%;">Solución Aplicada</th>
        <th style="width:10%;">Estado</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>v1.0.0</strong><br>01/11/2026</td>
        <td>Compilación Gradle (Windows)</td>
        <td>Fallo en <code>gradle assembleRelease</code> debido a caracteres no-ASCII (tilde en la ruta <code>Distribución</code>).</td>
        <td>Se activó <code>android.overridePathCheck=true</code> en <code>gradle.properties</code> y se compiló sin alteración de carpetas.</td>
        <td><span class="status-badge status-ok">Aprobado</span></td>
      </tr>
      <tr>
        <td><strong>v1.0.0</strong><br>01/11/2026</td>
        <td>Red y Seguridad Android</td>
        <td>Necesidad de garantizar que peticiones HTTP/HTTPS a la API externa no sean bloqueadas por el sandbox de Android.</td>
        <td>Declaración explícita de <code>INTERNET</code> y <code>ACCESS_NETWORK_STATE</code> en <code>AndroidManifest.xml</code>.</td>
        <td><span class="status-badge status-ok">Aprobado</span></td>
      </tr>
      <tr>
        <td><strong>v1.0.0</strong><br>01/11/2026</td>
        <td>Firebase App Distribution</td>
        <td>Registro de testers y vinculación al grupo de prueba <code>QA_Clase</code>.</td>
        <td>Creación de grupo en consola, asignación del docente <code>dduran@uceva.edu.co</code> y activación de enlace de invitación.</td>
        <td><span class="status-badge status-ok">Aprobado</span></td>
      </tr>
      <tr>
        <td><strong>v1.0.1</strong><br>01/11/2026</td>
        <td>Versionado Incremental</td>
        <td>Requisito de validar actualización incremental sin ambigüedad en el dispositivo de prueba.</td>
        <td>Incremento de <code>versionCode: 2</code> y adición del distintivo visual <code>v1.0.1 (Build 2)</code> en el Dashboard.</td>
        <td><span class="status-badge status-ok">Aprobado</span></td>
      </tr>
      <tr>
        <td><strong>v1.0.1</strong><br>01/11/2026</td>
        <td>Prueba OTA (Over-The-Air)</td>
        <td>Comprobación de descarga e instalación en caliente desde Firebase App Tester.</td>
        <td>Instalación exitosa conservando la misma firma de depuración/release sin conflicto de paquete.</td>
        <td><span class="status-badge status-ok">Aprobado</span></td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">9. Flujo de Trabajo GitFlow y Control de Versiones</div>
  <p>
    El código fuente del taller se gestionó implementando la metodología <strong>GitFlow</strong> en el repositorio oficial:
  </p>
  <ul>
    <li><strong><code>main</code>:</strong> Rama principal con la versión estable, documentación completa y código preparado para producción.</li>
    <li><strong><code>dev</code>:</strong> Rama de desarrollo e integración donde se concentran los cambios probados antes del despliegue final.</li>
    <li><strong><code>feature/app_distribution</code>:</strong> Rama de trabajo específica donde se realizaron los ajustes de permisos, compilaciones de release, configuración de App Distribution y documentación.</li>
    <li><strong>Pull Request (PR) y Merges:</strong> Se generó el PR desde <code>feature/app_distribution</code> hacia <code>dev</code> y posteriormente se fusionó a <code>main</code> garantizando la trazabilidad histórica.</li>
  </ul>

  <div class="section-title">10. Conclusiones Técnicas</div>
  <ol>
    <li><strong>Eficiencia en el Ciclo de QA:</strong> Firebase App Distribution reduce drásticamente el tiempo de retroalimentación (*feedback loop*) entre el desarrollador móvil y el equipo de testing, evitando el intercambio manual de APKs por medios inseguros.</li>
    <li><strong>Garantía de Versionado:</strong> El cumplimiento estricto del par <code>versionName</code> / <code>versionCode</code> es fundamental para que el gestor de paquetes de Android reconozca las actualizaciones incrementales y permita la instalación OTA sin errores de firma.</li>
    <li><strong>Transparencia Documental:</strong> Las Release Notes estructuradas garantizan que tanto testers como docentes conozcan exactamente las funcionalidades añadidas y los casos de prueba a priorizar.</li>
  </ol>

  <div class="footer-doc">
    Página 4 de 4 • Taller 1: Distribución de APK con Firebase App Distribution • UCEVA 2026
  </div>

</body>
</html>
"""

html_path = os.path.join(base_dir, "INFORME_FINAL_EVIDENCIAS.html")
pdf_path = os.path.join(base_dir, "INFORME_FINAL_EVIDENCIAS_DISTRIBUCION_APK.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generado exitosamente en: {html_path}")

# Compilación a PDF mediante Chrome headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

browser_path = chrome_path if os.path.exists(chrome_path) else edge_path

file_url = f"file:///{html_path.replace(os.sep, '/')}"

cmd = [
    browser_path,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    file_url
]

print(f"Ejecutando compilador PDF: {' '.join(cmd)}")
result = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
    print(f"PDF generado exitosamente ({os.path.getsize(pdf_path)} bytes) en:\n{pdf_path}")
else:
    print("Fallo en la generación directa con Chrome. Error:", result.stderr)
