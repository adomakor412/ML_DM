class HyperTan(object):
    
    def hypertan(x):
        if x < -20.0:
          return -1.0
        elif x > 20.0:
          return 1.0
        else:
          return math.tanh(x)
    
    def compute_output(self, x_value):
        hidden_sum = np.zeros(shape=[self.n_hidden], dtype=np.float32)
        output_sum = np.zeros(shape=[self.n_output], dtype=np.float32)

        for j in range(self.n_hidden):
            for i in range(self.n_input):
                hidden_sum[j] += self.input_node[i] * self.i2h_weight[i,j]

        for j in range(self.n_hidden):
          self.hidden_node[j] = self.hypertan(hidden_sum[j])


        return result