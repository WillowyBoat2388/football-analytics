import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # for col in data:
    #     df[col] = data[col].apply(eval)
    #     df = df.explode(col)
    # df['goals'] = data.goals.apply(eval)
    # df = df.explode('goals')

    #value = data['goals'].values
    # print(value)
    valuee = data.to_dict('records')
    # value = eval(value)
    #print (value)
    out = []
    for entry in valuee:
        # print(entry)
        for key, value in entry.items():
            if key == 'goals':
                # val = eval(value)
                # print (val)
                #print(value)
                for k, v in value.items():
                    #print (k , v)
                    #out = []
                    for k1, v1 in v.items():
                        for k2, v2 in v1.items():
                            #print(k2, v2)
                            result = (k, k1, k2, v2)
                            out.append(result)
    #print (out)
    df = pd.DataFrame(out, columns = ['goals.direction', 'goals.type', 'goals.location', 'goals'], dtype= 'str')
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
