test = {
  'name': 'Question 2.0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(open_drawers(10, 5, np.random.choice(np.arange(10), 10, replace=False), 0))
          5
          """,
          'hidden': False,
          'locked': False
        }      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
