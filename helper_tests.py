from helper import post_comment, read_gz, csv_to_dict, read_search

#===============================================================================
# post_comment
#===============================================================================
def test_post_comment():
    entity_key = 'http-requests'
    text = 'hey'
    # CALL
    response = post_comment(entity_key, text)
    
#test_post_comment()

#===============================================================================
# read_gz
#===============================================================================
def test_read_gz():
    file_path = 'sample_search_result/results.csv.gz'
    # CALL
    file_content = read_gz(file_path)
    # ASSERT
    assert "date_month" in file_content
    
#test_read_gz()

#===========================================================================
# csv_to_dict
#===========================================================================
def test_csv_to_dict():
    file_path = 'sample_search_result/results_preview.csv'
    # CALL
    content = csv_to_dict(file_path)
    # assert
    assert len(content) > 1
    assert (content[0]['success_count'] == '1573')
    
#test_csv_to_dict()

#===========================================================================
# read_search
#===========================================================================
def test_read_search():
    file_path = 'sample_search_result/results.csv.gz'
    # CALL
    content = read_search(file_path)
    # assert
    assert len(content) > 1
    assert (content[0]['success_count'] == '1573')
    
test_read_search()