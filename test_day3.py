import pytest


from log_parser import LogParser

@pytest.fixture
def Log1():
    return LogParser()

@pytest.mark.parametrize("line, expected",[
    ("[2026-10-19 12:00:00] [SUCCESS] User logged in", {"time": "2026-10-19 12:00:00", "status": "SUCCESS", "text": "User logged in"}),
    ("[2026-10-19 12:05:23] [ERROR] Connection lost to server", {"time": "2026-10-19 12:05:23", "status": "ERROR", "text": "Connection lost to server"}),
    ("[2026-10-19 12:10:15] [WARNING] Low disk space on /dev/sda1", {"time": "2026-10-19 12:10:15", "status": "WARNING", "text": "Low disk space on /dev/sda1"}),
     ("[2026-10-19 12:15:00] [ERROR] Database query timeouted", {"time": "2026-10-19 12:15:00", "status": "ERROR", "text": "Database query timeouted"}),
      ("[2026-10-19 12:20:44] [INFO] Background cron job finished successfully", {"time": "2026-10-19 12:20:44", "status": "INFO", "text": "Background cron job finished successfully"}),
       ("[2026-10-19 23:59:59] [SUCCESS] Daily backup created",  {"time": "2026-10-19 23:59:59", "status": "SUCCESS", "text": "Daily backup created"}  ),
        ("2026-10-19 12:00:00 [ERROR] Missing brackets in time log", None),
         ("[2026/10/19 12:00:00] [ERROR] Wrong date separators", None),
          ("[NOT_A_DATE 12:00:00] [ERROR] Broken timestamp text", None),
           ("[2026-10-19 12:00:00] Just random text without status", None),
            ("Short broken line", None)
]
)

def test_purse_line(Log1, line, expected):
    assert Log1.parse_line(line) == expected


@pytest.fixture
def sample_log_lines():

    return [
        "[2026-10-19 12:00:00] [SUCCESS] User logged in",
        "[2026-10-19 12:05:23] [ERROR] Connection lost to server",
        "[2026-10-19 12:10:15] [WARNING] Low disk space",
        "[2026-10-19 12:15:00] [ERROR] Database query timeouted",
        "[2026-10-19 12:20:44] [INFO] Cron job finished",
        "Short broken line"
    ]
def test_error_counter(Log1,sample_log_lines):
    assert Log1.count_errors(sample_log_lines) == 2