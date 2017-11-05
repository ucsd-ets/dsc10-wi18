test = {
  'name': 'Question 1.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> prisoner_table.num_rows
          10
          """,
          'hidden': False,
          'locked': False
        }, 
        {
          'code': r"""
          >>> prisoner_table.column('choices')[0][4] >= 0
          True
          """,
          'hidden': False,
          'locked': False
        }    ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
