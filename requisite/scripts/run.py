import sys, os

def run():
  base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  sys.path.insert(0, base)
  import requisite
  requisite.main()

if __name__ == '__main__':
  exit = run()
  if exit:
    sys.exit(exit)
