#!/usr/bin/env python3

import sys
sys.path.append('/home/usman/python-project-49/brain_games')

from cli import welcome_user
from brain_even import even_game


def main():
	welcome_user()
	even_game()


if __name__ == '__main__':
	main()
