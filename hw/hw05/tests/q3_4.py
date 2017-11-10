test = {
  'name': 'Question 1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 'int' in str(type(simulate()))
          True
          >>> # It looks like your simulation isn't random.
          >>> np.std([simulate() for _ in range(1000)]) > 0
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
