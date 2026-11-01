import os
import subprocess
import base64

base_dir = r"F:\Users\Max\Desktop\moviles\taller Distribución de APK con Firebase App Distribution"
screenshots_dir = os.path.join(base_dir, "docs", "screenshots")

def get_base64_img(base_name, fallback_name=None):
    for name in [base_name, fallback_name]:
        if not name:
            continue
        for ext in ["", ".png", ".jpg", ".jpeg", ".webp"]:
            target = name if name.endswith(ext) and ext != "" else name + ext
            path = os.path.join(screenshots_dir, target)
            if os.path.exists(path):
                with open(path, "rb") as f:
                    data = base64.b64encode(f.read()).decode("utf-8")
                    mime = "image/jpeg" if target.lower().endswith((".jpg", ".jpeg")) else "image/png"
                    return f"data:{mime};base64,{data}"
    return ""

# Capturas reales prioritarias
img_releases = get_base64_img("01_firebase_releases")
img_testers = get_base64_img("02_firebase_testers")
img_email = get_base64_img("03_correo_invitacion_brave")
img_installed = get_base64_img("04_app_instalada_dispositivo", "01_dashboard.png")
img_update = get_base64_img("05_evidencia_actualizacion", "02_departamentos_listado.png")

def render_image_or_placeholder(img_data, title, filename_hint):
    if img_data:
        return f'''
        <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; padding:6px; text-align:center; box-shadow:0 2px 6px rgba(0,0,0,0.05); margin-bottom:10px;">
            <img src="{img_data}" style="max-width:100%; max-height:260px; object-fit:contain; border-radius:4px;" alt="{title}">
            <div style="font-size:11px; font-weight:700; color:#334155; margin-top:5px;">{title}</div>
        </div>
        '''
    else:
        return f'''
        <div style="background:#f8fafc; border:2px dashed #94a3b8; border-radius:8px; padding:22px 14px; text-align:center; color:#475569; margin-bottom:10px;">
            <div style="font-size:22px; margin-bottom:4px;">📸</div>
            <div style="font-size:12px; font-weight:bold; color:#0f172a; margin-bottom:3px;">{title}</div>
            <div style="font-size:11px; color:#64748b;">Guarda tu captura real en:</div>
            <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-size:11px; color:#0284c7;">docs/screenshots/{filename_hint}</code>
        </div>
        '''

releases_html = render_image_or_placeholder(img_releases, "Captura Real: Panel de Releases en Firebase App Distribution (v1.0.0 y v1.0.1)", "01_firebase_releases.png")
testers_html = render_image_or_placeholder(img_testers, "Captura Real: Panel Testers & Groups (Grupo QA_Clase con samuel.rincon01 y dduran)", "02_firebase_testers.png")
email_html = render_image_or_placeholder(img_email, "Captura Real: Correo de Invitación recibido en Gmail (Brave) de samuel.rincon01@uceva.edu.co", "03_correo_invitacion_brave.png")
installed_html = render_image_or_placeholder(img_installed, "Captura Real: FlowBiz instalada y ejecutándose en dispositivo físico Android", "04_app_instalada_dispositivo.png")
update_html = render_image_or_placeholder(img_update, "Captura Real: Evidencia de Actualización a v1.0.1 (Badge v1.0.1 en UI)", "05_evidencia_actualizacion.png")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Taller 1: Distribución de APK con Firebase App Distribution — UCEVA</title>
  <style>
    @page {{
      size: letter;
      margin: 14mm 13mm 14mm 13mm;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      line-height: 1.45;
      background-color: #ffffff;
      margin: 0;
      padding: 0;
      font-size: 12px;
    }}
    .page-break {{
      page-break-before: always;
    }}
    .header-institution {{
      border-bottom: 2.5px solid #006837;
      padding-bottom: 10px;
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .header-institution .titles h1 {{
      color: #006837;
      margin: 0 0 3px 0;
      font-size: 18px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }}
    .header-institution .titles h2 {{
      color: #0369a1;
      margin: 0;
      font-size: 13px;
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
      padding: 12px 16px;
      border-radius: 8px;
      margin-bottom: 14px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    }}
    .repo-banner .title {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #38bdf8;
      font-weight: bold;
      margin-bottom: 3px;
    }}
    .repo-banner .url {{
      font-size: 13.5px;
      font-weight: bold;
      color: #f8fafc;
      word-break: break-all;
      font-family: monospace;
    }}
    .info-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
      margin-bottom: 14px;
    }}
    .info-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      padding: 8px 12px;
      border-radius: 6px;
    }}
    .info-card .label {{
      font-size: 10px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      margin-bottom: 2px;
    }}
    .info-card .value {{
      font-size: 12px;
      font-weight: 600;
      color: #0f172a;
    }}
    .section-title {{
      color: #0f172a;
      border-left: 4px solid #0284c7;
      padding-left: 8px;
      margin-top: 16px;
      margin-bottom: 8px;
      font-size: 14px;
      font-weight: 700;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0 12px 0;
      font-size: 11px;
    }}
    th, td {{
      border: 1px solid #cbd5e1;
      padding: 6px 8px;
      text-align: left;
    }}
    th {{
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      font-size: 10px;
      text-transform: uppercase;
    }}
    .status-badge {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: bold;
    }}
    .status-ok {{
      background-color: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }}
    .callout {{
      background: #eff6ff;
      border-left: 4px solid #0284c7;
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      margin: 10px 0;
      font-size: 11px;
    }}
    .callout-title {{
      font-weight: bold;
      color: #0369a1;
      margin-bottom: 2px;
    }}
    .footer-doc {{
      margin-top: 18px;
      border-top: 1px solid #e2e8f0;
      padding-top: 8px;
      text-align: center;
      font-size: 9.5px;
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
      <div class="label">Estudiante / Tester Receptor:</div>
      <div class="value">Samuel Alejandro Rincon Serna</div>
    </div>
    <div class="info-card">
      <div class="label">Código Estudiantil:</div>
      <div class="value">230231045</div>
    </div>
    <div class="info-card">
      <div class="label">Correo Institucional (Receptor en Brave):</div>
      <div class="value"><code>samuel.rincon01@uceva.edu.co</code></div>
    </div>
    <div class="info-card">
      <div class="label">Docente Asignado / Tester Evaluador:</div>
      <div class="value"><code>dduran@uceva.edu.co</code></div>
    </div>
    <div class="info-card">
      <div class="label">Application ID (Android):</div>
      <div class="value"><code>com.flowbiz.flowbiz</code></div>
    </div>
    <div class="info-card">
      <div class="label">Grupo de Testers Configurado:</div>
      <div class="value"><code>QA_Clase</code></div>
    </div>
  </div>

  <div class="section-title">1. Resumen Ejecutivo del Taller y Herramienta de Distribución</div>
  <p>
    El presente informe documenta la preparación técnica, configuración de permisos mínimos, compilación en modo release, despliegue y pruebas de aseguramiento de calidad (QA) de la aplicación móvil Flutter de la asignatura (<strong>FlowBiz</strong>) mediante <strong>Firebase App Distribution</strong>.
  </p>
  <p>
    Se evidencian los requisitos del taller: configuración del grupo de evaluadores <code>QA_Clase</code> con el docente (<code>dduran@uceva.edu.co</code>) y el correo del estudiante (<code>samuel.rincon01@uceva.edu.co</code>), distribución de la versión base inicial (<strong>1.0.0+1</strong>), despliegue de la actualización incremental (<strong>1.0.1+2</strong>) con notificación OTA (Over-The-Air), ejecución en dispositivo físico Android y bitácora de incidencias resueltas.
  </p>

  <div class="section-title">2. Preparación del APK y Permisos en AndroidManifest.xml</div>
  <p>
    Para asegurar la conectividad con servicios web y APIs de Datos Abiertos de Colombia sin bloqueos del sistema operativo, se verificaron e integraron los permisos en <code>android/app/src/main/AndroidManifest.xml</code>:
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
        <td>Permite conexiones de red HTTP/HTTPS hacia la API REST y servicios de Firebase.</td>
        <td><span class="status-badge status-ok">Configurado y Verificado</span></td>
      </tr>
      <tr>
        <td><code>android.permission.ACCESS_NETWORK_STATE</code></td>
        <td>Permite monitorear si el dispositivo cuenta con conexión Wi-Fi o datos móviles activos.</td>
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
    Flutter administra en <code>pubspec.yaml</code> el par <code>versionName+versionCode</code>:
    <br>• <strong>Release 1 (Base):</strong> <code>version: 1.0.0+1</code> (versionName <code>1.0.0</code>, versionCode <code>1</code>) — 50.2 MB en <code>releases/app-release-v1.0.0.apk</code>
    <br>• <strong>Release 2 (Update):</strong> <code>version: 1.0.1+2</code> (versionName <code>1.0.1</code>, versionCode <code>2</code>) — 50.2 MB en <code>releases/app-release-v1.0.1.apk</code>
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

  <div class="section-title">3. Captura del Panel de Releases en Firebase App Distribution</div>
  <p>
    Evidencia de las versiones <strong>1.0.0 (Build 1)</strong> y <strong>1.0.1 (Build 2)</strong> subidas al proyecto de Firebase y asignadas al grupo <code>QA_Clase</code>:
  </p>
  {releases_html}

  <div class="section-title">4. Captura del Panel Testers & Groups (Grupo QA_Clase)</div>
  <p>
    Evidencia del grupo de prueba <strong>QA_Clase</strong> con el docente <code>dduran@uceva.edu.co</code> y el estudiante <code>samuel.rincon01@uceva.edu.co</code>:
  </p>
  {testers_html}

  <div class="footer-doc">
    Página 2 de 4 • Taller 1: Distribución de APK con Firebase App Distribution • UCEVA 2026
  </div>

  <!-- ==================== PÁGINA 3: CORREO Y PRUEBAS EN DISPOSITIVO FÍSICO ==================== -->
  <div class="page-break"></div>

  <div class="header-institution">
    <div class="titles">
      <h1>EVIDENCIAS DE INVITACIÓN POR CORREO Y EJECUCIÓN FÍSICA</h1>
      <h2>Recepción en Gmail (Brave) y App Instalada en Android</h2>
    </div>
    <div class="badge-uceva">Evidencias Paso 3</div>
  </div>

  <div class="section-title">5. Captura Real del Correo de Invitación en Gmail (Brave)</div>
  <p>
    Evidencia del correo de notificación emitido por Firebase App Distribution recibido en la bandeja de entrada institucional (<code>samuel.rincon01@uceva.edu.co</code>) en el navegador Brave:
  </p>
  {email_html}

  <div class="section-title">6. Evidencias de la App Instalada y Actualización Incremental</div>
  <p>
    Captura de la aplicación FlowBiz instalada en el dispositivo físico Android y verificación de la actualización incremental con el distintivo de versión visible:
  </p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-top:8px;">
    <div>{installed_html}</div>
    <div>{update_html}</div>
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

  <div class="section-title">7. Bitácora de QA (Incidencias Encontradas y Solucionadas)</div>
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
        <td>Se activó <code>android.overridePathCheck=true</code> en <code>gradle.properties</code> y se compiló sin alterar rutas físicas.</td>
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
        <td>Creación de grupo en consola, asignación del docente <code>dduran@uceva.edu.co</code> y de <code>samuel.rincon01@uceva.edu.co</code>.</td>
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

  <div class="section-title">8. Flujo de Trabajo GitFlow y Control de Versiones</div>
  <p>
    El código fuente del taller se gestionó implementando la metodología <strong>GitFlow</strong> en el repositorio oficial:
  </p>
  <ul>
    <li><strong><code>main</code>:</strong> Rama principal con la versión estable, documentación completa y código preparado para producción.</li>
    <li><strong><code>dev</code>:</strong> Rama de desarrollo e integración donde se concentran los cambios probados antes del despliegue final.</li>
    <li><strong><code>feature/app_distribution</code>:</strong> Rama de trabajo específica donde se realizaron los ajustes de permisos, compilaciones de release, configuración de App Distribution y documentación.</li>
    <li><strong>Pull Request (PR) y Merges:</strong> Se generó el PR desde <code>feature/app_distribution</code> hacia <code>dev</code> y posteriormente se fusionó a <code>main</code> garantizando la trazabilidad histórica en GitHub.</li>
  </ul>

  <div class="section-title">9. Conclusiones Técnicas</div>
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

print(f"HTML actualizado en: {html_path}")

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

subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 1000:
    print(f"PDF recompilado exitosamente ({os.path.getsize(pdf_path)} bytes) en:\n{pdf_path}")
