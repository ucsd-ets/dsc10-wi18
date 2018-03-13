test = {
  'name': 'Question 1_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance(full_data, Table)
          True
          >>> 'PlayerName' in full_data.labels
          False
          >>> full_data_ref = player_data.join('Name', salary_data, 'PlayerName')
          >>> np.array_equal(full_data_ref.column('Name'), full_data.column('Name'))
          True
          >>> np.array_equal(full_data_ref.column('Age'), full_data.column('Age'))
          True
          >>> np.array_equal(full_data_ref.column('Points'), full_data.column('Points'))
          True
          >>> np.array_equal(full_data_ref.column('Salary'), full_data.column('Salary'))
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
