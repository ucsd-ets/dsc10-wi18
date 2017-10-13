test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> high_average_zips.sort('ZIP').take([0, 1, 2]).select('ZIP')
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> high_average_zips.num_rows != 0
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
