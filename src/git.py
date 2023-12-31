import enum
import subprocess


class KnownError(Exception):
    def __init__(self, message):
        self.message = message


class GitCommands(enum.Enum):
    REPO_TOPLEVEL = 'git rev-parse --show-toplevel'


def assert_git_repo():
    try:
        repo_toplevel = subprocess.check_output(GitCommands.REPO_TOPLEVEL.value, shell=True).strip().decode('utf-8')
        return repo_toplevel
    except subprocess.CalledProcessError:
        raise KnownError('The current directory must be a Git repository!')


def get_git_diff(file_name):
    command = ['git', 'diff', '--cached', '--diff-algorithm=minimal', file_name]
    result = subprocess.run(command, capture_output=True, text=True,encoding='utf-8')
    return result.stdout
