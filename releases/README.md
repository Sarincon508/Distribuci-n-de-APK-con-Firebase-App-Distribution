# 📦 FlowBiz - Archivos APK de Release

Este directorio contiene las compilaciones ejecutables APK preparadas y firmadas para su distribución mediante **Firebase App Distribution**.

## 📱 Compilaciones Disponibles

| Archivo APK | Versión | Build Code | Tamaño | Propósito |
| :--- | :---: | :---: | :---: | :--- |
| `app-release-v1.0.0.apk` | `1.0.0` | `1` | ~50.2 MB | **Versión Base Inicial:** Primer release distribuido al grupo `QA_Clase` con el explorador de Datos Abiertos de Colombia y permisos de red configurados. |
| `app-release-v1.0.1.apk` | `1.0.1` | `2` | ~50.2 MB | **Actualización Incremental:** Segundo release distribuido para validar el flujo de notificación OTA, actualización en vivo y visualización de versión en UI. |

---

## 🛠️ Comandos de Generación Utilizados

```bash
# Compilación Release Versión 1.0.0 (Build 1)
flutter build apk --release

# Compilación Release Versión 1.0.1 (Build 2)
flutter build apk --release
```

Ambos archivos se encuentran optimizados con R8/ProGuard y compresión de assets (`tree-shaken fonts`).
