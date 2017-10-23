test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> per_capita_usage.sort(0).relabeled(1, 'V').take([0, 1, 2]).num_rows > 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> per_capita_usage.num_rows != 0
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
