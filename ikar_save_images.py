from ikar_graphs import *
def save_all_images(user):

    if user.choice == 1 or user.choice == 4 or user.choice == 5:
        chess_scheme_with_a_wall_chb(user.D_k, user.H, user.number_pr, user.delta_wall, user.delta, user.delta_y_pr , user.choice ,user.second_layer,user.delete_center)
    elif user.choice == 2 or user.choice == 6 or user.choice == 7:
        cellular_scheme_with_a_wall_chb(user.D_k, user.H, user.number_pr, user.delta_wall, user.delta, user.delta_y_pr , user.choice ,user.second_layer,user.delete_center)
    elif user.choice == 3 or user.choice == 8 or user.choice == 9:
        concentric_scheme_with_a_wall_chb(user.D_k, user.H, user.number_pr, user.delta_wall, user.delta ,user.delta_y_pr, user.choice,user.second_layer,user.delete_center)
    elif user.choice == 10 or user.choice == 13 :
        chess_scheme_chb(user.D_k, user.H, user.delta_wall, user.delta, user.choice,user.delete_center)
    elif user.choice == 11 or user.choice == 14 :
        cellular_scheme_chb(user.D_k, user.H, user.delta_wall, user.delta, user.choice,user.delete_center)
    else:
        concentric_scheme_chb(user.D_k, user.H, user.delta_wall, user.delta, user.choice,user.delete_center)

    print_dot_chb(user.coord_graph, user.D_k, user.H, user.n)
    three_d_graph_chb(user.km_graph, user.D_k)
    three_d_graph_T_chb(user.T_graph, user.D_k)
    plt.show()