test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # order should be a list containing the numbers 1 through 7.
          >>> isinstance(order, list)
          True
          >>> order_ref = make_array(2, 7, 5, 6, 4, 1, 3)
          >>> np.array_equal(np.array(order).astype(int), order_ref)
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
