test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> income_by_zipcode.num_columns != 0
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> income_by_zipcode.num_rows != 0
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
