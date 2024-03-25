# Test data
test_data = [
    ("perf-20240318072606-JgS6n", "devnv_perf_20240318072606_JgS6n"),
    ("perf-20240318072605-NDsti", "devnv_perf_20240318072605_NDsti"),
    ("perf-20240318072609-aTfwR", "devnv_perf_20240318072609_aTfwR"),
    ("perf-20240318072604-c7ahV", "devnv_perf_20240318072604_c7ahV"),
    ("perf-20240318072605-IAz7t", "devnv_perf_20240318072605_IAz7t"),
    ("perf-20240318072606-4EYD4", "devnv_perf_20240318072606_4EYD4"),
    ("perf-20240318072605-IBwpg", "devnv_perf_20240318072605_IBwpg"),
    ("perf-20240318072604-mMGEH", "devnv_perf_20240318072604_mMGEH"),
    ("perf-20240318072604-Lxfki", "devnv_perf_20240318072604_Lxfki"),
    ("perf-20240318072604-dt7ka", "devnv_perf_20240318072604_dt7ka"),
    ("perf-20240318072605-GlDjQ", "devnv_perf_20240318072605_GlDjQ"),
    ("perf-20240318072610-D2tb9", "devnv_perf_20240318072610_D2tb9"),
    ("perf-20240318072604-efZQI", "devnv_perf_20240318072604_efZQI"),
    ("perf-20240318072605-94F9q", "devnv_perf_20240318072605_94F9q"),
    ("perf-20240318072604-4EPZF", "devnv_perf_20240318072604_4EPZF"),
    ("perf-20240318072604-vhPwX", "devnv_perf_20240318072604_vhPwX"),
    ("perf-20240318072554-pURns", "devnv_perf_20240318072554_pURns"),
    ("perf-20240318072508-bzHvJ", "devnv_perf_20240318072508_bzHvJ"),
    ("perf-20240318072401-pkij6", "devnv_perf_20240318072401_pkij6"),
    ("perf-20240318072349-8voME", "devnv_perf_20240318072349_8voME")
]

# Generate and print SQL scripts
for client_id, database_name in test_data:
    print(f"exec dbo.DropDatabase @clientID = '{client_id}', @database= '[{database_name}]'")
    print("\n")  # Separate scripts with a blank line
