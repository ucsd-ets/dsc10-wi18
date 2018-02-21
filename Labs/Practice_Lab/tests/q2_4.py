test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> seq_123([1, 1, 2, 3, 1]) == True
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> seq_123([1, 1, 2, 4, 1])  == False
          True
          """,
          'hidden': False,
          'locked': False
        },
          {
          'code': r"""
          >>> seq_123([1, 1, 2, 4, 3])  == True
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