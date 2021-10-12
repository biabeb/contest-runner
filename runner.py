#!/usr/bin/python

import sys
import subprocess
import json
import difflib
import textwrap
from pathlib import Path

USAGE = """usage: runner run <problem name> <solution file> [<test index>]
       runner input <problem name> <test case index>
       runner output <problem name> <text case index>

runner is a script that runs test cases for programming contest problems. Use
the first form to run all test cases for a problem. Use the second form to
print the input that is provided to the solution for the given test case, and
use the third form to print the expected output for the given test case."""
PROBLEMS = Path('db/problems')

class Problem:
    def __init__(self, path: Path, json: dict):
        self._path = path
        self.id = json['id']
        self.title = json['title']
        self.tests = json['tests']
        self.description = json['description']
        self.statement = json['statement']
        self.input = json['input']
        self.output = json['output']
        self.constraints = json['constraints']


    def load_input(self, index: int):
        if index >= self.tests:
            raise Exception()

        try:
            with self._path.joinpath('input', f'in{index}.txt').open() as input_file:
                return input_file.read()
        except:
            return None


    def load_output(self, index: int):
        if index >= self.tests:
            raise Exception()

        try:
            with self._path.joinpath('output', f'out{index}.txt').open() as output_file:
                return output_file.read()
        except:
            return None
        

def load_db():
    db = {}

    for problem_dir in PROBLEMS.iterdir():
        problem_desc_path = problem_dir.joinpath('problem.json')
        try:
            with problem_desc_path.open() as problem_desc_file:
                problem = Problem(problem_dir, json.load(problem_desc_file))
                db[problem.id] = problem
        except Exception as e:
            print(f"warning: failed to load problem with id '{problem_dir.name}'")
            print(f"         due to exception {e}")
            continue

    return db


def run_test(problem: Problem, test: int, solution: str):
    input_text = problem.load_input(test)
    output_text = problem.load_output(test)

    completed = subprocess.run(['python', solution], input = input_text, capture_output = True, text = True)

    return completed.stdout == output_text, difflib.unified_diff(completed.stdout.splitlines(keepends = True), output_text.splitlines(keepends = True), fromfile = 'your solution\'s output', tofile = 'expected output')


def run_show_test(problem: Problem, test: int, solution: str):
    justified = str(test_index).rjust(len(str(problem.tests - 1)))

    passed, diff = run_test(problem, test_index, solution_filename)

    if passed:
        print(f'Test case {justified}: PASS')
    else:
        print(f'Test case {justified}: FAIL')
        print('-------------diff-------------')
        print(''.join(diff), end = '')
        print('-----------end diff-----------')


def load_problem(db, title):
    for problem in db.values():
        if problem.title == title:
            return problem
    sys.exit(f"error: unknown problem '{title}'")

def main():
    if len(sys.argv) < 2:
        sys.exit(USAGE)
    action = sys.argv[1]

    problem = None

    db = load_db()

    if action == 'run':
        if len(sys.argv) == 4:
            problem = load_problem(db, sys.argv[2])
            solution_filename = sys.argv[3]
            for test_index in range(problem.tests):
                run_show_test(problem, test_index, solution_filename)
        elif len(sys.argv) == 5:
            problem = load_problem(db, sys.argv[2])
            solution_filename = sys.argv[3]
            test_index = int(sys.argv[4])
            run_show_test(problem, test_index, solution_filename)            
        else:
            sys.exit(USAGE)
    elif action == 'input':
        if len(sys.argv) != 4:
            sys.exit(USAGE)
        problem = load_problem(db, sys.argv[2])
        test_index = sys.argv[3]

        print(problem.load_input(int(test_index)), end = '')
    elif action == 'output':
        if len(sys.argv) != 4:
            sys.exit(USAGE)
        problem = load_problem(db, sys.argv[2])
        test_index = sys.argv[3]

        print(problem.load_output(int(test_index)), end = '')
    elif action == 'list':
        for problem in db.values():
            print(problem.title)
    elif action == 'desc':
        if len(sys.argv) != 3:
            sys.exit(USAGE)
        problem = load_problem(db, sys.argv[2])

        print(problem.title)
        print()
        print("Description:")
        print(textwrap.indent(problem.description, '  '))
        print("Statement:")
        print(textwrap.indent(problem.statement, '  '))
        print("Input:")
        print(textwrap.indent(problem.input, '  '))
        print("Output:")
        print(textwrap.indent(problem.output, '  '))
        print("Constraints:")
        print(textwrap.indent(problem.constraints.replace("&lt;", "<").replace("&gt;", ">").replace("&le;", "<=").replace("&ge;", ">="), '  '))
    elif action == 'dump':
        for problem in db.values():
            md = f"""# {problem.title}
## Description
{problem.description}

## Statement
{problem.statement}

## Input
{problem.input}

## Output
{problem.output}

## Constraints
{problem.constraints}"""
            with open(f'{problem.title}.md', 'w') as f:
                f.write(md)
    else:
        sys.exit(f"error: unknown action '{action}'")


if __name__ == "__main__":
    main()
