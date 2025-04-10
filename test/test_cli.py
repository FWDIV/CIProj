import pytest
import sys
import os
import argparse
from ciproject.cli import make_parser

def test_parse_exists():
    parser = make_parser()
    assert parser != None

def simulate_cli_input(parser,monkeypatch, args_input):
    monkeypatch.setattr("sys.argv", args_input)
    return parser.parse_args()


@pytest.mark.parametrize( "args_input, expected",
        [
            (["<ignored script name>","add", "new task 1"], {"desc":"new task 1","id":None}),
            (["<ignored script name>","add", "new task 1", "--id","432"],{"desc":"new task 1","id":432})
        ]
)
def test_add_parse(monkeypatch,args_input,expected):
    parser = make_parser()
    args = simulate_cli_input(parser,monkeypatch,args_input)
    assert args.desc == expected["desc"]
    assert args.id == expected["id"]

@pytest.mark.parametrize("args_input, expected",
                        [
                            (["<ignored script name>","delete","432"],{"id":432})
                        ])
def test_delete_parse(monkeypatch,args_input,expected):
    parser = make_parser()
    args = simulate_cli_input(parser,monkeypatch,args_input)
    assert args.id == expected["id"]