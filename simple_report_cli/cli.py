import click
import os
from simple_report_cli import build_report, print_report


def get_file_content(folder_path, filename, insert_char=False, char='', pos=0):
    """Get data from file"""

    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r') as f:
        if insert_char:
            lines = f.readlines()
            lines_new = []
            for line in lines:
                lines_new.append(f'{line[:pos]}{char}{line[pos:]}')
            content = ''.join(lines_new)
            return content
        else:
            content = f.read()
            return content


@click.command()
@click.option('--files', required=True, type=click.Path(
    exists=True, file_okay=False, dir_okay=True,
    readable=True, resolve_path=True), help='Path to folder with files')
@click.option('--driver', help='Driver name.')
@click.option('--asc', is_flag=True, help='Order asc.')
@click.option('--desc', is_flag=True, help='Order desc.')
def main(files, driver, asc, desc):
    """The program that print the report of Monaco 2018 Racing."""

    data = {'abb': get_file_content(files, 'abbreviations.txt'),
            'start': get_file_content(files, 'start.log', True, '_', 3),
            'end': get_file_content(files, 'end.log', True, '_', 3)}

    if asc and desc:
        print('asc/desc: Only one option can be used!')
        return
    elif asc:
        report = build_report(data, True)
    elif desc:
        report = build_report(data, False)
    else:
        report = build_report(data)

    if asc or desc:
        print_report(report, driver)
    else:
        print_report(report, driver, True)


if __name__ == '__main__':
    main()
