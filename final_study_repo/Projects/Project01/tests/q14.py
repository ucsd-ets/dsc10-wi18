test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> income.num_rows != 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> int(max(income.column('returns'))) != 0
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
