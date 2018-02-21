test = {
  'name': 'Question 2_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> temp_converter(100) == 27
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> temp_converter(100, direction=False) == 212
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