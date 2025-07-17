# Simple real-world program demonstrating Python data types

# 1. Numeric data types
patient_age = 28            # int
temperature = 37.5          # float
pulse = 80 + 0j             # complex (used rarely, for demo)

# 2. String data type
patient_name = "Davelyn Gitayee"
report_title = f"Health Report for {patient_name}"

# 3. Sequence data types
symptoms = ["fever", "headache", "fatigue"]
visited_dates = ("2025-07-07", "2025-07-08")

# 4. Combine into report string
report = f"""
{report_title}
Age: {patient_age}
Temperature: {temperature}°C
Symptoms: {', '.join(symptoms)}
Visits: {', '.join(visited_dates)}
"""

print("📝 Full Report:")
print(report)

# 5. Convert report to bytes for storage
report_bytes = bytearray(report, 'utf-8')
print("\n📦 Encoded Report (bytearray):", report_bytes[:50], "...")

# 6. Use memoryview to change 'D' in Davelyn to 'M' (simulate name correction)
mv = memoryview(report_bytes)
mv[report.find("D")] = ord('M')  # Replace 'D' with 'M'

# 7. Decode updated bytearray
updated_report = report_bytes.decode('utf-8')

print("\n✅ Updated Report After Memoryview Edit:")
print(updated_report)
