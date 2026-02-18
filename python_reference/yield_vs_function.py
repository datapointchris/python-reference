import random
import string
from collections.abc import Generator
from datetime import datetime
from pathlib import Path


class LogGenerator:
    LOG_TYPES: dict = {}

    def generate(self, log_type: str, number: int) -> Generator[str]:
        for _ in range(number):
            # Generate log data based on log_type
            if log_type == 'access':
                method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
                endpoint = random.choice(['/home', '/about', '/contact'])
                status_code = random.randint(200, 500)
                response_time = random.randint(100, 10000)
                browser = random.choice(['Chrome', 'Firefox', 'Safari', 'Edge'])
                yield f'{method} {endpoint} {status_code} {response_time} {browser}'

            elif log_type == 'error':
                level = random.choice(['ERROR', 'WARNING', 'INFO'])
                error_type = random.choice(['File not found', 'Syntax error', 'Database connection error'])
                line_number = random.randint(1, 100)
                file_name = random.choice(['app.py', 'database.py', 'utils.py'])
                yield f'{level}: {error_type} at line {line_number} in {file_name}'

            elif log_type == 'security':
                event_type = random.choice(['LOGIN', 'LOGOUT', 'PASSWORD_CHANGE'])
                user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                ip_address = '.'.join(str(random.randint(0, 255)) for _ in range(4))
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                yield f'{event_type} {user_id} {ip_address} {timestamp}'
            else:
                # Invalid log_type
                raise ValueError('Invalid log_type')

    def to_file(self, log_type, number, file_name):
        with open(file_name, 'w') as f:
            for log in self.generate(log_type, number):
                f.write(log + '\n')


log_gen = LogGenerator()

for log in log_gen.generate('access', 10):
    print(log)

for log in log_gen.generate('error', 10):
    print(log)

for log in log_gen.generate('security', 10):
    print(log)

log_gen.to_file('error', 100_000, 'large_log_file.log')


def yield_lines_from(file_path: Path | str) -> Generator[str]:
    with open(file_path) as file:
        for line in file:
            yield line.strip()


def parse_error_log(log_line: str):
    log_data: dict[str, str | int] = {}
    log_parts = log_line.split(': ')
    log_data['level'] = log_parts[0]
    error_parts = log_parts[1].split(' at line ')
    log_data['error_type'] = error_parts[0]
    line_parts = error_parts[1].split(' in ')
    log_data['line_number'] = int(line_parts[0])
    log_data['file_name'] = line_parts[1]
    yield log_data


def process_lines(lines: Generator[str]) -> Generator[dict]:
    for line in lines:
        yield from parse_error_log(line)


for i, data in enumerate(process_lines(yield_lines_from('large_log_file.log'))):
    if i > 10:
        break
    # Process data further
    print(data)
