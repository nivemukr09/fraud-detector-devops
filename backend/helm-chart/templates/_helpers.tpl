{{- define "fraud-detector.name" -}}
{{- .Chart.Name -}}
{{- end }}

{{- define "fraud-detector.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "fraud-detector.labels" -}}
app.kubernetes.io/name: {{ include "fraud-detector.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{- define "fraud-detector.serviceAccountName" -}}
{{- if .Values.serviceAccount.name }}
{{- .Values.serviceAccount.name }}
{{- else }}
{{- printf "%s-%s" .Release.Name "serviceaccount" | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

