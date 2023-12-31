from typing import Dict

commit_type_formats: Dict[str, str] = {
    '': '<commit message>',
    'conventional': '<type>(<optional scope>): <commit message>',
}


def specify_commit_format(commit_type: str) -> str:
    return 'The output response must be in format:\n{}'.format(commit_type_formats[commit_type])


commit_types: Dict[str, str] = {
    '': '',
    'conventional': "Choose a type from the type-to-description JSON below that best describes the git diff:\n{}".format(
        {
            'docs': 'Documentation only changes',
            'style': 'Changes that do not affect the meaning of the code (white-space, formatting, missing '
                     'semi-colons, etc)',
            'refactor': 'A code change that neither fixes a bug nor adds a feature',
            'perf': 'A code change that improves performance',
            'test': 'Adding missing tests or correcting existing tests',
            'build': 'Changes that affect the build system or external dependencies',
            'ci': 'Changes to our CI configuration files and scripts',
            'chore': "Other changes that don't modify src or test files",
            'revert': 'Reverts a previous commit',
            'feat': 'A new feature',
            'fix': 'A bug fix',
        }
    ),
}


def generate_prompt(locale: str, max_length: int, commit_type: str) -> str:
    message_parts = [
        'Generate a concise git commit message written in present tense for the following code diff with the given '
        'specifications below:',
        'Message language: {}'.format(locale),
        'Commit message must be a maximum of {} characters.'.format(max_length),
        'Exclude anything unnecessary such as translation. Your entire response will be passed directly into git '
        'commit.',
        commit_types[commit_type],
        specify_commit_format(commit_type),
    ]
    return '\n'.join(part for part in message_parts if part)
