test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(missing, np.ndarray)
          True
          >>> missing_ref = make_array(14, 33, 35, 57, 60, 76, 80, 81, 85, 96, 102, 103, 130, 143, 178, 181, 186, 210, 215, 227, 247, 258, 264, 270, 272, 294, 319, 344, 354, 358)
          >>> set(missing_ref) == set(missing)
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
